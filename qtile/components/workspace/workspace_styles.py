"""
Configuración de estilos para el Workspace Grid
Tema monocromático consistente con la configuración de qtile
"""

class WorkspaceStyles:
    """Clase con todos los estilos para el workspace grid"""
    
    # ====== [COLORES PRINCIPALES] ======
    # Basados en el tema monocromático existente
    BACKGROUND = "#0c0c0c"           # Fondo principal
    BACKGROUND_ALPHA = "#0c0c0cE6"   # Fondo con transparencia (90%)
    
    CONTAINER_BG = "#18181840"       # Fondo de contenedores
    CONTAINER_BORDER = "#ffffff66"   # Borde de contenedores (40% alpha)
    CONTAINER_BORDER_ACTIVE = "#ffffff" # Borde cuando está seleccionado
    
    TEXT_PRIMARY = "#ffffff"         # Texto principal
    TEXT_SECONDARY = "#cccccc"       # Texto secundario  
    TEXT_INACTIVE = "#666666"        # Texto inactivo
    TEXT_MUTED = "#444444"           # Texto muy tenue
    
    # ====== [COLORES DE WORKSPACES] ======
    WORKSPACE_ACTIVE = "#ffffff"     # Workspace actual
    WORKSPACE_OCCUPIED = "#cccccc"   # Workspace con ventanas
    WORKSPACE_EMPTY = "#666666"      # Workspace vacío
    
    # ====== [DIMENSIONES] ======
    WINDOW_WIDTH = 1200              # Ancho total de la ventana
    WINDOW_HEIGHT = 400              # Alto total de la ventana
    
    CONTAINER_PADDING = 20           # Padding interno de contenedores
    CONTAINER_SPACING = 15           # Espacio entre contenedores
    CONTAINER_BORDER_WIDTH = 2       # Grosor del borde
    CONTAINER_RADIUS = 12            # Radio de esquinas (simulado)
    
    LEFT_CONTAINER_WIDTH = 200       # Ancho del contenedor izquierdo (20%)
    RIGHT_CONTAINER_WIDTH = 950      # Ancho del contenedor derecho (80%)
    
    # ====== [FUENTES] ======
    FONT_FAMILY = "Hack Nerd Font"
    FONT_SIZE_LARGE = 14
    FONT_SIZE_NORMAL = 12
    FONT_SIZE_SMALL = 10
    
    # ====== [POSICIONAMIENTO] ======
    WINDOW_POSITION_Y_OFFSET = 100  # Distancia desde abajo
    
    @classmethod
    def get_container_style(cls):
        """Retorna el estilo base para contenedores"""
        return {
            'bg': cls.CONTAINER_BG,
            'highlightbackground': cls.CONTAINER_BORDER,
            'highlightthickness': cls.CONTAINER_BORDER_WIDTH,
            'relief': 'flat',
            'bd': 0
        }
    
    @classmethod
    def get_text_style(cls, text_type="normal"):
        """Retorna el estilo para texto según el tipo"""
        color_map = {
            'primary': cls.TEXT_PRIMARY,
            'secondary': cls.TEXT_SECONDARY,
            'inactive': cls.TEXT_INACTIVE,
            'muted': cls.TEXT_MUTED
        }
        
        size_map = {
            'large': cls.FONT_SIZE_LARGE,
            'normal': cls.FONT_SIZE_NORMAL,
            'small': cls.FONT_SIZE_SMALL
        }
        
        return {
            'fg': color_map.get(text_type, cls.TEXT_PRIMARY),
            'bg': cls.CONTAINER_BG,
            'font': (cls.FONT_FAMILY, size_map.get('normal', cls.FONT_SIZE_NORMAL)),
            'relief': 'flat',
            'bd': 0
        }
    
    @classmethod
    def get_workspace_style(cls, state="empty"):
        """Retorna el estilo para workspaces según su estado"""
        color_map = {
            'active': cls.WORKSPACE_ACTIVE,
            'occupied': cls.WORKSPACE_OCCUPIED, 
            'empty': cls.WORKSPACE_EMPTY
        }
        
        return {
            'fg': color_map.get(state, cls.WORKSPACE_EMPTY),
            'bg': cls.CONTAINER_BG,
            'font': (cls.FONT_FAMILY, cls.FONT_SIZE_NORMAL, 'bold'),
            'relief': 'flat',
            'bd': 0
        }