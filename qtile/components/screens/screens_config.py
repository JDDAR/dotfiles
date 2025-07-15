"""
Configuración de pantallas para Qtile
"""

from libqtile.config import Screen
from components.bar.bar_config import get_primary_bar, get_secondary_bar

def get_screens():
    """
    Retorna la configuración de pantallas
    La primera pantalla (principal) tiene Systray, las demás no
    """
    screens = [
        # ====== [PANTALLA PRINCIPAL] ======
        Screen(
            top=get_primary_bar(),  # Con Systray
            wallpaper=None,         # El fondo se maneja desde background_config
            wallpaper_mode='fill',
        ),
        
        # ====== [PANTALLA SECUNDARIA] ======
        Screen(
            top=get_secondary_bar(),  # Sin Systray
            wallpaper=None,           # El fondo se maneja desde background_config
            wallpaper_mode='fill',
        ),
    ]
    
    return screens

# Exportamos para usar en config.py
screens = get_screens()