"""
Configuración de layouts (diseños de ventanas) para Qtile
"""

from libqtile import layout

def get_layouts():
    """
    Retorna la lista de layouts configurados
    """
    # Configuración de colores para los layouts
    layout_theme = {
        "border_width": 2,
        "margin": 8,
        "border_focus": "#e1acff",      # Púrpura claro para ventana activa
        "border_normal": "#1D2330",     # Gris oscuro para ventanas inactivas
    }
    
    layouts = [
        # ====== [LAYOUT MAX] ======
        # Ventanas ocupan toda la pantalla (ideal para navegadores, editores)
        layout.Max(),
        
        # ====== [LAYOUT MONAD TALL] ======
        # Una ventana principal a la izquierda, otras apiladas a la derecha
        layout.MonadTall(
            **layout_theme,
            single_border_width=0,      # Sin borde cuando hay una sola ventana
            single_margin=0,            # Sin margen cuando hay una sola ventana
        ),
        
        # ====== [LAYOUT COLUMNS] ======
        # Múltiples columnas, útil para muchas ventanas
        layout.Columns(
            **layout_theme,
            num_columns=3,              # Máximo 3 columnas
            split=False,                # No dividir automáticamente
        ),
        
        # ====== [LAYOUT TREE TAB] ======
        # Pestañas en la parte superior, útil para organización
        layout.TreeTab(
            font="Hack Nerd Font",
            fontsize=12,
            sections=["FIRST", "SECOND", "THIRD"],
            section_fontsize=11,
            border_width=2,
            bg_color="1c1f24",
            active_bg="c678dd",
            active_fg="000000",
            inactive_bg="a9a1e1",
            inactive_fg="1c1f24",
            padding_left=0,
            padding_x=0,
            padding_y=5,
            section_top=10,
            section_bottom=20,
            level_shift=8,
            vspace=3,
            panel_width=200
        ),
        
        # ====== [LAYOUT FLOATING] ======
        # Para ventanas flotantes (se configura por separado en floating_config)
        layout.Floating(**layout_theme),
    ]
    
    return layouts

# Exportamos para usar en config.py
layouts = get_layouts()