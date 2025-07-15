"""
Configuración del ratón para Qtile
"""

from libqtile.config import Click, Drag
from libqtile.lazy import lazy

# Configuración básica
mod = "mod4"

def get_mouse_config():
    """
    Retorna la configuración del ratón
    """
    mouse = [
        # ====== [ARRASTRAR VENTANAS] ======
        # Mod + Click izquierdo: Mover ventana flotante
        Drag([mod], "Button1", 
             lazy.window.set_position_floating(),
             start=lazy.window.get_position()),
        
        # Mod + Click derecho: Redimensionar ventana flotante
        Drag([mod], "Button3", 
             lazy.window.set_size_floating(),
             start=lazy.window.get_size()),
        
        # ====== [CLICKS] ======
        # Mod + Click medio: Traer ventana al frente
        Click([mod], "Button2", 
              lazy.window.bring_to_front()),
    ]
    
    return mouse

# Configuraciones adicionales del ratón
def get_mouse_settings():
    """
    Retorna configuraciones adicionales del comportamiento del ratón
    """
    settings = {
        "follow_mouse_focus": True,      # El foco sigue al ratón
        "bring_front_click": False,      # Click no trae ventana al frente automáticamente
        "cursor_warp": False,            # El cursor no salta al enfocar ventanas
    }
    
    return settings

# Exportamos para usar en config.py
mouse = get_mouse_config()
mouse_settings = get_mouse_settings()