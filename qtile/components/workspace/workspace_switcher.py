"""
Workspace Switcher - VERSIÓN SÚPER SIMPLE
Solo mostrar DOS contenedores
"""

import tkinter as tk
import threading
from libqtile.lazy import lazy

@lazy.function
def show_workspace_grid_tk(qtile):
    """
    Función SÚPER SIMPLE - solo mostrar dos contenedores
    """
    try:
        print("🚀 Iniciando contenedor simple...")
        
        def create_simple_window():
            # Crear ventana principal
            root = tk.Tk()
            root.title("Workspace Grid")
            root.geometry("1200x400")
            
            # Configurar ventana
            root.overrideredirect(True)  # Sin decoraciones
            root.attributes('-topmost', True)  # Siempre encima
            root.configure(bg='#0c0c0c')
            
            # Posicionar en la parte inferior
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width - 1200) // 2
            y = screen_height - 400 - 100
            root.geometry(f"+{x}+{y}")
            
            # Frame principal
            main_frame = tk.Frame(root, bg='#0c0c0c', padx=20, pady=20)
            main_frame.pack(fill=tk.BOTH, expand=True)
            
            # Contenedor izquierdo
            left_container = tk.Frame(
                main_frame,
                bg='#18181840',
                width=200,
                height=300,
                highlightbackground='#ffffff66',
                highlightthickness=2,
                relief='flat'
            )
            left_container.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 15))
            left_container.pack_propagate(False)
            
            # Texto en contenedor izquierdo
            left_label = tk.Label(
                left_container,
                text="Contenedor 1",
                fg='#ffffff',
                bg='#18181840',
                font=('Hack Nerd Font', 14)
            )
            left_label.pack(expand=True)
            
            # Contenedor derecho
            right_container = tk.Frame(
                main_frame,
                bg='#18181840',
                height=300,
                highlightbackground='#ffffff66',
                highlightthickness=2,
                relief='flat'
            )
            right_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
            # Texto en contenedor derecho
            right_label = tk.Label(
                right_container,
                text="Contenedor 2",
                fg='#ffffff',
                bg='#18181840',
                font=('Hack Nerd Font', 14)
            )
            right_label.pack(expand=True)
            
            # Cerrar con Escape
            root.bind('<Escape>', lambda e: root.destroy())
            root.bind('<Button-1>', lambda e: root.destroy())
            
            # Auto-cerrar después de 5 segundos
            root.after(5000, root.destroy)
            
            # Mostrar ventana
            root.focus_force()
            root.mainloop()
        
        # Ejecutar en thread separado
        thread = threading.Thread(target=create_simple_window, daemon=True)
        thread.start()
        
        print("✅ Ventana simple iniciada")
        
    except Exception as e:
        print(f"💥 Error: {e}")
        import traceback
        traceback.print_exc()