"""
Interfaz Tkinter para el Workspace Grid
Crea los dos contenedores lado a lado como en la imagen
"""

import tkinter as tk
from tkinter import ttk
import threading
import time

from .workspace_styles import WorkspaceStyles
from .workspace_data import WorkspaceDataProvider

class TkinterWorkspaceGrid:
    """Interfaz principal del workspace grid con Tkinter"""
    
    def __init__(self, qtile):
        self.qtile = qtile
        self.data_provider = WorkspaceDataProvider(qtile)
        self.styles = WorkspaceStyles
        self.root = None
        self.is_visible = False
        
    def show(self):
        """Muestra el workspace grid"""
        if self.is_visible:
            return
        
        try:
            self._create_window()
            self._setup_layout()
            self._populate_content()
            self._show_window()
            
        except Exception as e:
            print(f"Error showing workspace grid: {e}")
            import traceback
            traceback.print_exc()
    
    def hide(self):
        """Oculta el workspace grid"""
        if self.root:
            self.root.destroy()
            self.root = None
        self.is_visible = False
    
    def _create_window(self):
        """Crea la ventana principal"""
        self.root = tk.Tk()
        
        # Configuración básica de ventana
        self.root.title("Workspace Grid")
        self.root.geometry(f"{self.styles.WINDOW_WIDTH}x{self.styles.WINDOW_HEIGHT}")
        
        # Configurar ventana como overlay
        self.root.overrideredirect(True)  # Sin decoraciones
        self.root.attributes('-topmost', True)  # Siempre encima
        self.root.configure(bg=self.styles.BACKGROUND)
        
        # Intentar transparencia (puede no funcionar en todos los WM)
        try:
            self.root.attributes('-alpha', 0.95)
        except:
            pass
        
        # Posicionar en la parte inferior de la pantalla
        self._position_window()
        
        # Binding para cerrar con Escape
        self.root.bind('<Escape>', lambda e: self.hide())
        self.root.bind('<Button-1>', self._on_click_outside)
        
        # Focus para capturar teclas
        self.root.focus_force()
    
    def _position_window(self):
        """Posiciona la ventana en la parte inferior de la pantalla"""
        # Obtener dimensiones de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calcular posición centrada en la parte inferior
        x = (screen_width - self.styles.WINDOW_WIDTH) // 2
        y = screen_height - self.styles.WINDOW_HEIGHT - self.styles.WINDOW_POSITION_Y_OFFSET
        
        self.root.geometry(f"+{x}+{y}")
    
    def _setup_layout(self):
        """Configura el layout principal con dos contenedores"""
        # Frame principal
        main_frame = tk.Frame(
            self.root, 
            bg=self.styles.BACKGROUND,
            padx=20,
            pady=20
        )
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Contenedor izquierdo (20% - Lista de workspaces)
        self.left_container = tk.Frame(
            main_frame,
            width=self.styles.LEFT_CONTAINER_WIDTH,
            **self.styles.get_container_style()
        )
        self.left_container.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, self.styles.CONTAINER_SPACING))
        self.left_container.pack_propagate(False)  # Mantener tamaño fijo
        
        # Contenedor derecho (80% - Preview del workspace)
        self.right_container = tk.Frame(
            main_frame,
            **self.styles.get_container_style()
        )
        self.right_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Agregar padding interno a los contenedores
        self.left_content = tk.Frame(
            self.left_container,
            bg=self.styles.CONTAINER_BG,
            padx=self.styles.CONTAINER_PADDING,
            pady=self.styles.CONTAINER_PADDING
        )
        self.left_content.pack(fill=tk.BOTH, expand=True)
        
        self.right_content = tk.Frame(
            self.right_container,
            bg=self.styles.CONTAINER_BG,
            padx=self.styles.CONTAINER_PADDING,
            pady=self.styles.CONTAINER_PADDING
        )
        self.right_content.pack(fill=tk.BOTH, expand=True)
    
    def _populate_content(self):
        """Llena los contenedores con contenido"""
        self._populate_left_container()
        self._populate_right_container()
    
    def _populate_left_container(self):
        """Llena el contenedor izquierdo con la lista de workspaces"""
        # Título del contenedor
        title_label = tk.Label(
            self.left_content,
            text="Workspaces",
            **self.styles.get_text_style('primary'),
            font=(self.styles.FONT_FAMILY, self.styles.FONT_SIZE_LARGE, 'bold')
        )
        title_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Lista de workspaces
        workspaces = self.data_provider.get_workspaces_info()
        
        for workspace in workspaces:
            self._create_workspace_item(workspace)
    
    def _create_workspace_item(self, workspace):
        """Crea un item de workspace en el contenedor izquierdo"""
        # Frame para el workspace
        workspace_frame = tk.Frame(self.left_content, bg=self.styles.CONTAINER_BG)
        workspace_frame.pack(fill=tk.X, pady=2)
        
        # Símbolo de estado
        if workspace['state'] == 'active':
            symbol = "●"
        elif workspace['state'] == 'occupied':
            symbol = "○"
        else:
            symbol = "◌"
        
        # Crear el label del workspace
        workspace_text = f"{symbol} {workspace['number']}"
        
        workspace_label = tk.Label(
            workspace_frame,
            text=workspace_text,
            **self.styles.get_workspace_style(workspace['state']),
            cursor="hand2"
        )
        workspace_label.pack(anchor=tk.W)
        
        # Binding para click
        workspace_label.bind('<Button-1>', 
            lambda e, num=workspace['number']: self._on_workspace_click(num))
    
    def _populate_right_container(self):
        """Llena el contenedor derecho con el preview del workspace actual"""
        preview_data = self.data_provider.get_current_workspace_preview()
        
        # Título del workspace actual
        title_text = f"Workspace {preview_data['number']}"
        title_label = tk.Label(
            self.right_content,
            text=title_text,
            **self.styles.get_text_style('primary'),
            font=(self.styles.FONT_FAMILY, self.styles.FONT_SIZE_LARGE, 'bold')
        )
        title_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Subtítulo con número de ventanas
        if preview_data['is_empty']:
            subtitle_text = "Empty workspace"
            subtitle_color = 'inactive'
        else:
            subtitle_text = f"{preview_data['window_count']} window(s) open"
            subtitle_color = 'secondary'
        
        subtitle_label = tk.Label(
            self.right_content,
            text=subtitle_text,
            **self.styles.get_text_style(subtitle_color),
            font=(self.styles.FONT_FAMILY, self.styles.FONT_SIZE_SMALL)
        )
        subtitle_label.pack(anchor=tk.W, pady=(0, 15))
        
        # Lista de ventanas
        if not preview_data['is_empty']:
            self._create_windows_list(preview_data['windows'])
    
    def _create_windows_list(self, windows):
        """Crea la lista de ventanas en el preview"""
        for window in windows[:6]:  # Máximo 6 ventanas
            window_frame = tk.Frame(self.right_content, bg=self.styles.CONTAINER_BG)
            window_frame.pack(fill=tk.X, pady=2)
            
            window_text = f"{window['icon']} {window['name']}"
            
            window_label = tk.Label(
                window_frame,
                text=window_text,
                **self.styles.get_text_style('secondary')
            )
            window_label.pack(anchor=tk.W)
        
        # Si hay más ventanas, mostrar indicador
        if len(windows) > 6:
            more_label = tk.Label(
                self.right_content,
                text=f"... and {len(windows) - 6} more",
                **self.styles.get_text_style('muted'),
                font=(self.styles.FONT_FAMILY, self.styles.FONT_SIZE_SMALL, 'italic')
            )
            more_label.pack(anchor=tk.W, pady=5)
    
    def _on_workspace_click(self, workspace_number):
        """Maneja el click en un workspace"""
        print(f"Switching to workspace {workspace_number}")
        success = self.data_provider.switch_to_workspace(workspace_number)
        if success:
            # Cerrar la ventana después de cambiar
            self.root.after(100, self.hide)  # Delay pequeño para transición suave
    
    def _on_click_outside(self, event):
        """Maneja clicks fuera de los contenedores para cerrar"""
        # Solo cerrar si el click fue en el fondo, no en los contenedores
        if event.widget == self.root:
            self.hide()
    
    def _show_window(self):
        """Muestra la ventana y maneja el loop principal"""
        self.is_visible = True
        
        # Auto-cerrar después de 10 segundos (timeout de seguridad)
        self.root.after(10000, self.hide)
        
        # Mostrar ventana
        self.root.mainloop()