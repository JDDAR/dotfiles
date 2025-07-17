"""
Configuración de ventanas flotantes para Qtile
"""

from libqtile import layout
from libqtile.config import Match

def get_floating_layout():
    """
    Retorna la configuración del layout flotante
    """
    # Tema visual para ventanas flotantes
    floating_theme = {
        "border_width": 2,
        "border_focus": "#e1acff",      # Púrpura claro para ventana activa
        "border_normal": "#1D2330",     # Gris oscuro para ventanas inactivas
        "max_border_width": 0,          # Sin borde en ventanas maximizadas
    }
    
    # Reglas para ventanas que deben ser flotantes automáticamente
    float_rules = [
        # ====== [DIÁLOGOS DEL SISTEMA] ======
        Match(wm_class="confirm"),          # Diálogos de confirmación
        Match(wm_class="dialog"),           # Diálogos generales
        Match(wm_class="download"),         # Ventanas de descarga
        Match(wm_class="error"),            # Ventanas de error
        Match(wm_class="file_progress"),    # Barras de progreso de archivos
        Match(wm_class="notification"),     # Notificaciones
        Match(wm_class="splash"),           # Pantallas de inicio
        Match(wm_class="toolbar"),          # Barras de herramientas
        
        # ====== [APLICACIONES ESPECÍFICAS] ======
        Match(wm_class="Arandr"),           # Configurador de pantallas
        Match(wm_class="Blueman-manager"),  # Gestor de Bluetooth
        Match(wm_class="Gpick"),            # Selector de colores
        Match(wm_class="Kruler"),           # Regla de pantalla
        Match(wm_class="MessageWin"),       # Ventanas de mensaje
        Match(wm_class="Sxiv"),             # Visor de imágenes
        Match(wm_class="Wpa_gui"),          # Configurador WiFi
        Match(wm_class="veromix"),          # Mezclador de audio
        Match(wm_class="xtightvncviewer"),  # Cliente VNC
        
        # ====== [VENTANAS DE CONFIGURACIÓN] ======
        Match(wm_class="Pavucontrol"),      # Control de volumen
        Match(wm_class="qt5ct"),            # Configurador Qt5
        Match(wm_class="Qtconfig-qt4"),     # Configurador Qt4
        
        # ====== [TÍTULOS ESPECÍFICOS] ======
        Match(title="branchdialog"),        # Diálogos de Git
        Match(title="pinentry"),            # Entrada de PIN/contraseña
        Match(title="Preferences"),         # Ventanas de preferencias
        Match(title="Settings"),            # Ventanas de configuración
        
        # ====== [ROLES DE VENTANA] ======
        Match(wm_type="utility"),           # Ventanas de utilidad
        Match(wm_type="notification"),      # Notificaciones del sistema
        Match(wm_type="toolbar"),           # Barras de herramientas
        Match(wm_type="splash"),            # Pantallas de bienvenida
        Match(wm_type="dialog"),            # Diálogos

        # ====== [GEMINI CLI MODAL] ======
        Match(title="gemini-cli-window"),   # Nuestra ventana de Gemini
    ]
    
    # Crear el layout flotante
    floating_layout = layout.Floating(
        float_rules=float_rules,
        **floating_theme
    )
    
    return floating_layout

floating_layout = get_floating_layout()