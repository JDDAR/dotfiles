import os
import subprocess
from libqtile import bar, hook, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import time

# Importamos las configuraciones desde components
from components.bar.bar_config import get_bar
from components.background.background_config import configure_background
from components.display.display_config import configure_displays, get_connected_monitors

# ====== [NUEVAS IMPORTACIONES] ======
from components.keybindings.keys_config import keys
from components.groups.groups_config import groups, group_keys
from components.layouts.layouts_config import layouts
from components.screens.screens_config import screens
from components.system.widget_defaults import widget_defaults, extension_defaults
from components.system.mouse_config import mouse, mouse_settings
from components.system.floating_config import floating_layout
from components.hooks.hooks_config import setup_hooks, qtile_settings

# ====== [CONFIGURACIÓN BÁSICA] ======
mod = "mod4"  # Tecla Super/Windows
terminal = guess_terminal()  # Detecta Alacritty automáticamente

# ====== [ATAJOS DE TECLADO] ======
# Las keys ahora se importan desde keys_config.py y groups_config.py
# Combinamos las teclas de navegación con las teclas de grupos
keys.extend(group_keys)

# ====== [GRUPOS (WORKSPACES)] ======
# Los grupos ahora se importan desde groups_config.py
# groups = [...] ← Esto ya no va aquí

# ====== [LAYOUTS] ======
# Los layouts ahora se importan desde layouts_config.py
# layouts = [...] ← Esto ya no va aquí

# ====== [PANTALLAS] ======
# screens ahora se importa desde screens_config.py
# screens = [...] ← Esto ya no va aquí

# ====== [CONFIGURACIÓN ADICIONAL] ======
# mouse, floating_layout y configuraciones adicionales ahora se importan desde system/
# Aplicamos las configuraciones del ratón
follow_mouse_focus = mouse_settings["follow_mouse_focus"]
bring_front_click = mouse_settings["bring_front_click"]
cursor_warp = mouse_settings["cursor_warp"]

# ====== [HOOKS Y CONFIGURACIÓN FINAL] ======
# Configurar todos los hooks del sistema
setup_hooks()

# Aplicar configuraciones adicionales de Qtile
dgroups_key_binder = qtile_settings["dgroups_key_binder"]
dgroups_app_rules = qtile_settings["dgroups_app_rules"]
auto_fullscreen = qtile_settings["auto_fullscreen"]
focus_on_window_activation = qtile_settings["focus_on_window_activation"]
reconfigure_screens = qtile_settings["reconfigure_screens"]
auto_minimize = qtile_settings["auto_minimize"]
wl_input_rules = qtile_settings["wl_input_rules"]
wmname = qtile_settings["wmname"]