"""
Configuración de la barra superior para Qtile
"""

from libqtile import bar, widget

def get_primary_bar():
    """
    Retorna la barra para la pantalla PRINCIPAL (con Systray)
    """
    return bar.Bar(
        [
            # ====== [LADO IZQUIERDO] ======
            widget.CurrentLayout(
                font="Hack Nerd Font Bold",
                fontsize=12,
                foreground="#e1acff",
            ),
            widget.Sep(
                linewidth=1,
                padding=10,
                foreground="#444444",
            ),
            widget.GroupBox(
                font="Hack Nerd Font",
                fontsize=14,
                margin_y=3,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active="#ffffff",
                inactive="#444444",
                rounded=False,
                highlight_method="line",
                highlight_color=["#0f0f0f", "#0f0f0f"],
                this_current_screen_border="#e1acff",
                this_screen_border="#e1acff",
            ),
            widget.Prompt(
                font="Hack Nerd Font",
                fontsize=14,
                foreground="#e1acff",
            ),
            widget.WindowName(
                font="Hack Nerd Font",
                fontsize=12,
                foreground="#ffffff",
                max_chars=50,
            ),

            # ====== [LADO DERECHO] ======
            widget.Systray(
                icon_size=20,
                padding=10,
            ),
            widget.Sep(
                linewidth=1,
                padding=10,
                foreground="#444444",
            ),
            widget.CPU(
                font="Hack Nerd Font",
                fontsize=12,
                foreground="#61afef",
                format=" {load_percent}%",
                update_interval=2,
            ),
            widget.Memory(
                font="Hack Nerd Font",
                fontsize=12,
                foreground="#98c379",
                format=" {MemUsed:.0f}{mm}",
                update_interval=2,
            ),
            widget.Volume(
                font="Hack Nerd Font",
                fontsize=12,
                foreground="#e06c75",
                fmt=" {}",
            ),
            widget.Battery(
                font="Hack Nerd Font",
                fontsize=12,
                foreground="#d19a66",
                format="{char} {percent:2.0%}",
                charge_char="",
                discharge_char="",
                full_char="",
                unknown_char="",
                empty_char="",
                update_interval=60,
            ),
            widget.Clock(
                font="Hack Nerd Font Bold",
                fontsize=12,
                foreground="#e1acff",
                format=" %H:%M  %d/%m/%Y",
            ),
            widget.QuickExit(
                font="Hack Nerd Font",
                fontsize=14,
                foreground="#e06c75",
                default_text="⏻",
                countdown_format="{}",
            ),
        ],
        24,  # Altura de la barra
        background="#0f0f0f",
        opacity=0.95,
    )

def get_secondary_bar():
    """
    Retorna la barra para pantallas SECUNDARIAS (sin Systray)
    """
    return bar.Bar(
        [
            # ====== [LADO IZQUIERDO] ======
            widget.CurrentLayout(
                font="Hack Nerd Font Bold",
                fontsize=12,
                foreground="#e1acff",
            ),
            widget.Sep(
                linewidth=1,
                padding=10,
                foreground="#444444",
            ),
            widget.GroupBox(
                font="Hack Nerd Font",
                fontsize=14,
                margin_y=3,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active="#ffffff",
                inactive="#444444",
                rounded=False,
                highlight_method="line",
                highlight_color=["#0f0f0f", "#0f0f0f"],
                this_current_screen_border="#e1acff",
                this_screen_border="#e1acff",
            ),
            widget.WindowName(
                font="Hack Nerd Font",
                fontsize=12,
                foreground="#ffffff",
                max_chars=50,
            ),

            # ====== [LADO DERECHO] ======
            # Sin Systray - solo información básica
            widget.Clock(
                font="Hack Nerd Font Bold",
                fontsize=12,
                foreground="#e1acff",
                format=" %H:%M",
            ),
        ],
        24,  # Altura de la barra
        background="#0f0f0f",
        opacity=0.95,
    )

# Función legacy para compatibilidad (mantener por ahora)
def get_bar():
    """
    Función de compatibilidad - retorna la barra principal
    """
    return get_primary_bar()