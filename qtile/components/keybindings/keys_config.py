"""
Configuración de atajos de teclado para Qtile
"""

import os
from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Configuración básica que necesitamos aquí
mod = "mod4"  # Tecla Super/Windows
terminal = guess_terminal()  # Detecta Alacritty automáticamente

def get_keys():
    """
    Retorna la lista de atajos de teclado configurados
    """
    keys = [
        # ====== [ROFI Y MENÚS] ======
        Key(["mod4"], "r", 
            lazy.spawn("rofi -show drun -theme ~/.config/rofi/themes/components/launchers/style-5.rasi"), 
            desc="Lanzar Rofi para aplicaciones"),
        
        Key([mod], "F8", 
            lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/display_menu.sh")), 
            desc="Menú de configuración de pantallas"),
        
        Key([mod], "w", 
            lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/wallpaper_menu.sh")), 
            desc="Menú de selección de wallpapers"),

        # ====== [TERMINAL Y CONTROL BÁSICO] ======
        Key([mod], "Return", 
            lazy.spawn(terminal), 
            desc="Abrir terminal"),
        
        Key([mod], "q", 
            lazy.window.kill(), 
            desc="Cerrar ventana"),
        
        Key([mod, "control"], "r", 
            lazy.reload_config(), 
            desc="Recargar Qtile"),
        
        Key([mod, "control"], "q", 
            lazy.shutdown(), 
            desc="Cerrar Qtile"),

        # ====== [NAVEGACIÓN DE VENTANAS] ======
        Key([mod], "h", 
            lazy.layout.left(), 
            desc="Mover foco a la izquierda"),
        
        Key([mod], "l", 
            lazy.layout.right(), 
            desc="Mover foco a la derecha"),
        
        Key([mod], "j", 
            lazy.layout.down(), 
            desc="Mover foco hacia abajo"),
        
        Key([mod], "k", 
            lazy.layout.up(), 
            desc="Mover foco hacia arriba"),
        
        Key([mod], "space", 
            lazy.layout.next(), 
            desc="Mover foco a la siguiente ventana"),

        # ====== [MOVER VENTANAS] ======
        Key([mod, "shift"], "h", 
            lazy.layout.shuffle_left(), 
            desc="Mover ventana a la izquierda"),
        
        Key([mod, "shift"], "l", 
            lazy.layout.shuffle_right(), 
            desc="Mover ventana a la derecha"),
        
        Key([mod, "shift"], "j", 
            lazy.layout.shuffle_down(), 
            desc="Mover ventana hacia abajo"),
        
        Key([mod, "shift"], "k", 
            lazy.layout.shuffle_up(), 
            desc="Mover ventana hacia arriba"),

        # ====== [REDIMENSIONAR VENTANAS] ======
        Key([mod, "control"], "h", 
            lazy.layout.grow_left(), 
            desc="Expandir ventana a la izquierda"),
        
        Key([mod, "control"], "l", 
            lazy.layout.grow_right(), 
            desc="Expandir ventana a la derecha"),
        
        Key([mod, "control"], "j", 
            lazy.layout.grow_down(), 
            desc="Expandir ventana hacia abajo"),
        
        Key([mod, "control"], "k", 
            lazy.layout.grow_up(), 
            desc="Expandir ventana hacia arriba"),
        
        Key([mod], "n", 
            lazy.layout.normalize(), 
            desc="Resetear tamaños de ventanas"),

        # ====== [CONTROL DE LAYOUTS] ======
        Key([mod], "Tab", 
            lazy.next_layout(), 
            desc="Alternar entre layouts"),
        
        Key([mod], "t", 
            lazy.window.toggle_floating(), 
            desc="Alternar modo flotante"),
        
        Key([mod], "f", 
            lazy.window.toggle_fullscreen(), 
            desc="Alternar pantalla completa"),

        # ====== [CONTROL DE VOLUMEN] ======
        Key([], "XF86AudioRaiseVolume", 
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"), 
            desc="Subir volumen"),
        
        Key([], "XF86AudioLowerVolume", 
            lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"), 
            desc="Bajar volumen"),
        
        Key([], "XF86AudioMute", 
            lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), 
            desc="Silenciar/Activar sonido"),

        # ====== [CONTROL DE BRILLO] ======
        Key([], "XF86MonBrightnessUp", 
            lazy.spawn("brightnessctl set +10%"), 
            desc="Aumentar brillo"),
        
        Key([], "XF86MonBrightnessDown", 
            lazy.spawn("brightnessctl set 10%-"), 
            desc="Disminuir brillo"),

        # ====== [CAPTURAS DE PANTALLA] ======
        Key([], "Print", 
            lazy.spawn("flameshot gui"), 
            desc="Captura de pantalla con selección"),
        
        Key(["shift"], "Print", 
            lazy.spawn("flameshot full -p ~/Pictures/Screenshots/"), 
            desc="Captura de pantalla completa"),
    ]
    
    return keys

# Exportamos la función para usar en config.py
keys = get_keys()