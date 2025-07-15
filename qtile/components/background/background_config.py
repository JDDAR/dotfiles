import subprocess
import os
from libqtile import hook


def configure_background():
    """Configura el fondo de pantalla, el teclado y picom al iniciar Qtile."""
    @hook.subscribe.startup_once
    def start_once():
        # Configurar el teclado en español
        subprocess.call(["setxkbmap", "es"])
        # Establecer el fondo de pantalla
        subprocess.call(["feh", "--bg-scale", os.path.expanduser(
            "~/Imágenes/wallpaper/RHCP.jpg")])
        # Iniciar picom para efectos visuales
        #subprocess.call(["picom", "--config", os.path.expanduser(
        #    "~/.config/picom/picom.conf")])
