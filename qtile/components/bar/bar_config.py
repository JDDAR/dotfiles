"""
Configuración moderna de la barra superior para Qtile
Tema monocromático con Nerd Fonts
"""

from libqtile import bar, widget
import os
import subprocess

# ====== [CONFIGURACIÓN DE COLORES MONOCROMÁTICO] ======
class MonochromeScheme:
    """Esquema de colores monocromático elegante"""
    
    # Colores de fondo (adaptados para Picom blur)
    BAR_BACKGROUND = "#0c0c0c80"      # Negro casi puro con transparencia
    WIDGET_BACKGROUND = "#18181880"   # Gris muy oscuro con transparencia
    
    # Escala de grises para texto
    TEXT_PRIMARY = "#ffffff"          # Blanco puro
    TEXT_SECONDARY = "#cccccc"        # Gris claro
    TEXT_TERTIARY = "#999999"         # Gris medio
    TEXT_INACTIVE = "#666666"         # Gris oscuro
    TEXT_DISABLED = "#444444"         # Gris muy oscuro
    
    # Acentos sutiles (mantienen la monocromía)
    ACCENT_BRIGHT = "#ffffff"         # Blanco para elementos importantes
    ACCENT_NORMAL = "#cccccc"         # Gris claro para elementos normales
    ACCENT_SUBTLE = "#999999"         # Gris medio para elementos secundarios
    ACCENT_MUTED = "#666666"          # Gris oscuro para elementos terciarios
    
    # Colores de separadores y bordes
    SEPARATOR = "#333333"             # Gris oscuro para separadores
    BORDER_ACTIVE = "#ffffff"         # Blanco para bordes activos
    BORDER_INACTIVE = "#555555"       # Gris medio para bordes inactivos
    
    # Estados especiales
    WARNING = "#cccccc"               # Gris claro para warnings
    ERROR = "#ffffff"                 # Blanco para errores (destacado)
    SUCCESS = "#cccccc"               # Gris claro para éxito

# ====== [CONFIGURACIÓN DE WIDGETS] ======
def create_left_widgets():
    """Widgets del lado izquierdo de la barra"""
    return [
        # Logo/Launcher con ícono Nerd Font
        widget.TextBox(
            text="",  # nf-linux-archlinux
            font="Hack Nerd Font",
            fontsize=16,
            foreground=MonochromeScheme.ACCENT_BRIGHT,
            padding=12,
            mouse_callbacks={
                'Button1': lambda: os.system("rofi -show drun -theme ~/.config/rofi/themes/components/launchers/style-5.rasi")
            }
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=8,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # Layout actual con ícono Nerd Font
        widget.CurrentLayout(
            font="Hack Nerd Font",
            fontsize=11,
            foreground=MonochromeScheme.ACCENT_NORMAL,
            padding=6,
            fmt="󰕮"  # nf-md-view_dashboard
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=8,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # GroupBox (Workspaces) con estilo monocromático
        widget.GroupBox(
            font="Hack Nerd Font",
            fontsize=11,
            margin_y=3,
            margin_x=0,
            padding_y=4,
            padding_x=4,
            borderwidth=1,
            
            # Colores monocromáticos
            active=MonochromeScheme.TEXT_PRIMARY,           # Grupo con ventanas
            inactive=MonochromeScheme.TEXT_INACTIVE,        # Grupo sin ventanas
            this_current_screen_border=MonochromeScheme.BORDER_ACTIVE,  # Grupo actual
            this_screen_border=MonochromeScheme.BORDER_ACTIVE,
            other_current_screen_border=MonochromeScheme.BORDER_INACTIVE,
            other_screen_border=MonochromeScheme.BORDER_INACTIVE,
            
            # Estilo visual minimalista
            rounded=False,
            highlight_method="line",
            highlight_color=[MonochromeScheme.BAR_BACKGROUND, MonochromeScheme.BAR_BACKGROUND],
            disable_drag=True,
            use_mouse_wheel=False,
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=8,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # Prompt para comandos
        widget.Prompt(
            font="Hack Nerd Font",
            fontsize=11,
            foreground=MonochromeScheme.ACCENT_NORMAL,
            prompt="󰅂 ",  # nf-md-chevron_right
            padding=4,
        ),
        
        # Nombre de ventana actual
        widget.WindowName(
            font="Hack Nerd Font",
            fontsize=11,
            foreground=MonochromeScheme.TEXT_SECONDARY,
            max_chars=50,
            padding=8,
            format="{name}",
            empty_group_string="Desktop"
        ),
        
        # Spacer para empujar widgets a la derecha
        widget.Spacer(),
    ]

def create_right_widgets():
    """Widgets del lado derecho de la barra"""
    return [
        # CPU con ícono Nerd Font
        widget.CPU(
            font="Hack Nerd Font",
            fontsize=12,
            foreground=MonochromeScheme.ACCENT_NORMAL,
            format="  {load_percent:04.1f}%",  # nf-md-cpu_64_bit
            update_interval=2.0,
            padding=6,
            mouse_callbacks={
                'Button1': lambda: os.system("alacritty -e htop")
            }
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=6,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # Memoria con ícono Nerd Font
        widget.Memory(
            font="Hack Nerd Font",
            fontsize=12,
            foreground=MonochromeScheme.ACCENT_NORMAL,
            format="  {MemUsed: .0f}{mm} ({MemPercent:.0f}%) ",  # nf-md-memory - Muestra usado y porcentaje
            update_interval=2.0,
            padding=6,
            mouse_callbacks={
                'Button1': lambda: os.system("alacritty -e htop")
            }
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=6,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # Red con ícono Nerd Font
        widget.Net(
            font="Hack Nerd Font",
            fontsize=12,
            foreground=MonochromeScheme.ACCENT_NORMAL,
            format=" {down}  {up}",  # nf-md-wifi
            update_interval=2.0,
            padding=6,
            mouse_callbacks={
                'Button1': lambda: os.system("nm-connection-editor")
            }
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=6,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # Volumen con ícono Nerd Font
        widget.Volume(
            font="Hack Nerd Font",
            fontsize=12,
            foreground=MonochromeScheme.ACCENT_NORMAL,
            fmt="  {}",  # nf-md-volume_high
            padding=6,
            mouse_callbacks={
                'Button1': lambda: os.system("pavucontrol"),
                'Button3': lambda: os.system("pactl set-sink-mute @DEFAULT_SINK@ toggle")
            }
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=6,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # Batería con ícono Nerd Font
        widget.GenPollText(
            func=lambda: subprocess.check_output(os.path.expanduser("~/.config/qtile/scripts/qtile-battery-status.sh")).decode("utf-8").strip(),
            update_interval=5, # Actualiza cada 5 segundos para dinamismo
            font="Hack Nerd Font",
            fontsize=12,
            padding=6,
            mouse_callbacks={
                'Button1': lambda: os.system("xfce4-power-manager-settings")
            }
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=6,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # Systray
        widget.Systray(
            icon_size=16,
            padding=6,
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=6,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # Reloj con ícono Nerd Font
        widget.Clock(
            font="Hack Nerd Font",
            fontsize=12,
            foreground=MonochromeScheme.ACCENT_BRIGHT,
            format="%H:%M  %d/%m",  # nf-md-clock_outline + nf-md-calendar
            padding=8,
            mouse_callbacks={
                'Button1': lambda: os.system("gnome-calendar")
            }
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=6,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # Botón de salida con ícono Nerd Font
        widget.QuickExit(
            font="Hack Nerd Font",
            fontsize=12,
            foreground=MonochromeScheme.ACCENT_SUBTLE,
            default_text=" ",  # nf-md-power
            countdown_format="{}",
            countdown_start=3,
            padding=8,
        ),
    ]

def get_primary_bar():
    """
    Retorna la barra para la pantalla PRINCIPAL (con Systray)
    Optimizada para Picom blur y tema monocromático
    """
    return bar.Bar(
        create_left_widgets() + create_right_widgets(),
        
        # Configuración visual minimalista
        size=28,                              # Altura óptima para minimalismo
        background=MonochromeScheme.BAR_BACKGROUND, # Fondo negro transparente
        opacity=1.0,                          # Picom maneja la transparencia
        margin=[0, 0, 0, 0],                  # Sin márgenes para look limpio
        border_width=[0, 0, 1, 0],            # Línea sutil inferior
        border_color=MonochromeScheme.SEPARATOR, # Color del borde
    )

def get_secondary_bar():
    """
    Retorna la barra para pantallas SECUNDARIAS (sin Systray)
    """
    # Widgets esenciales para pantallas secundarias
    right_widgets_minimal = [
        # CPU
        widget.CPU(
            font="Hack Nerd Font",
            fontsize=12,
            foreground=MonochromeScheme.ACCENT_NORMAL,
            format=" {load_percent:04.1f}%",
            update_interval=2.0,
            padding=6,
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=6,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # Memoria
        widget.Memory(
            font="Hack Nerd Font",
            fontsize=12,
            foreground=MonochromeScheme.ACCENT_NORMAL,
            format=" {MemUsed:.1f}{mm}",
            update_interval=2.0,
            padding=6,
        ),
        
        # Separador
        widget.Sep(
            linewidth=1,
            padding=6,
            foreground=MonochromeScheme.SEPARATOR,
            size_percent=70
        ),
        
        # Reloj
        widget.Clock(
            font="Hack Nerd Font",
            fontsize=11,
            foreground=MonochromeScheme.ACCENT_BRIGHT,
            format=" %H:%M",
            padding=8,
        ),
    ]
    
    return bar.Bar(
        create_left_widgets() + right_widgets_minimal,
        
        # Configuración visual minimalista
        size=28,                              # Altura óptima para minimalismo
        background=MonochromeScheme.BAR_BACKGROUND, # Fondo negro transparente
        opacity=1.0,                          # Picom maneja la transparencia
        margin=[0, 0, 0, 0],                  # Sin márgenes para look limpio
        border_width=[0, 0, 1, 0],            # Línea sutil inferior
        border_color=MonochromeScheme.SEPARATOR, # Color del borde
    )

# Función legacy para compatibilidad
def get_bar():
    """
    Función de compatibilidad - retorna la barra principal
    """
    return get_primary_bar()