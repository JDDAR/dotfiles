"""
Configuración por defecto de widgets para Qtile
"""

def get_widget_defaults():
    """
    Retorna la configuración por defecto para todos los widgets
    """
    widget_defaults = {
        "font": "Hack Nerd Font",       # Fuente con íconos
        "fontsize": 14,                 # Tamaño de fuente
        "padding": 5,                   # Espaciado interno
        "foreground": "#ffffff",        # Color de texto por defecto
        "background": None,             # Fondo transparente por defecto
    }
    
    return widget_defaults

def get_extension_defaults():
    """
    Configuración por defecto para extensiones de widgets
    """
    # Los extension_defaults suelen ser iguales a widget_defaults
    return get_widget_defaults()

# Exportamos para usar en config.py
widget_defaults = get_widget_defaults()
extension_defaults = get_extension_defaults()