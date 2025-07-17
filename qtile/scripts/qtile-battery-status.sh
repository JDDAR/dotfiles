#!/bin/bash

# Script para obtener el estado de la batería con colores dinámicos para Qtile (usando Pango markup)

# Colores en formato HEX (de tu MonochromeScheme)
COLOR_RED="#f38ba8"     # Rojo (usando el color de error de tu esquema)
COLOR_YELLOW="#f9e2af"  # Amarillo (usando el color de advertencia de tu esquema)
COLOR_GREEN="#a6e3a1"   # Verde (un verde suave)
COLOR_BLUE="#89b4fa"    # Azul (para cargando)
COLOR_DEFAULT="#cccccc" # Gris claro (TEXT_SECONDARY de tu esquema)

# Iconos Nerd Font
ICON_CHARGING="󰂄" # nf-md-battery_charging
ICON_FULL="󰁹"     # nf-md-battery_full
ICON_HIGH="󰁽"     # nf-md-battery_80
ICON_MEDIUM="󰁿"   # nf-md-battery_60
ICON_LOW="󰁻"      # nf-md-battery_20
ICON_EMPTY="󰂎"    # nf-md-battery_empty
ICON_UNKNOWN="󰂑"   # nf-md-battery_unknown

# Obtener estado de la batería
BATTERY_STATUS=$(cat /sys/class/power_supply/BAT0/status 2>/dev/null)
BATTERY_CAPACITY=$(cat /sys/class/power_supply/BAT0/capacity 2>/dev/null)

# Si no hay batería (ej. desktop), salir
if [ -z "$BATTERY_CAPACITY" ]; then
    echo ""
    exit 0
fi

COLOR="$COLOR_DEFAULT"
ICON="$ICON_UNKNOWN"

if [ "$BATTERY_STATUS" = "Charging" ]; then
    COLOR="$COLOR_BLUE"
    ICON="$ICON_CHARGING"
elif [ "$BATTERY_STATUS" = "Full" ]; then
    COLOR="$COLOR_GREEN"
    ICON="$ICON_FULL"
elif [ "$BATTERY_STATUS" = "Discharging" ]; then
    if [ "$BATTERY_CAPACITY" -le 20 ]; then
        COLOR="$COLOR_RED"
        ICON="$ICON_LOW"
    elif [ "$BATTERY_CAPACITY" -le 40 ]; then
        COLOR="$COLOR_YELLOW"
        ICON="$ICON_LOW"
    elif [ "$BATTERY_CAPACITY" -le 60 ]; then
        ICON="$ICON_MEDIUM"
    elif [ "$BATTERY_CAPACITY" -le 80 ]; then
        ICON="$ICON_HIGH"
    else
        ICON="$ICON_FULL"
    fi
fi

# Imprimir el resultado con Pango markup
# <span foreground="#HEXCOLOR">TEXTO</span>
echo "<span foreground=\"${COLOR}\">${ICON} ${BATTERY_CAPACITY}%</span>"