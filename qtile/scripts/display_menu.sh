#!/bin/bash

# Obteniendo monitores detectados
PRIMARY="eDP1"
EXTERNAL=$(xrandr --query | grep " connected" | grep -v "$PRIMARY" | awk '{print $1}')

# Si no hay monitores externos utiliza la pantalla principal
if [ -z "$EXTERNAL" ]; then
    xrandr --output "$PRIMARY" --auto
    qtile cmd-obj -o cmd -f reconfigure_screens
    notify-send "Display" "Solo pantalla principal detectada"
    exit 0
fi

# Opciones del menú
OPTIONS="Solo interna\nSolo externa\nEspejo\nExtendida derecha\nExtendida izquierda\nExtendida arriba\nExtendida abajo"

# Mostrar menú con rofi y capturar la selección
CHOICE=$(echo -e "$OPTIONS" | rofi -dmenu -p "Configurar pantallas")

# Ejecutar la configuración según la elección
case "$CHOICE" in
    "Solo interna")
        xrandr --output "$PRIMARY" --auto --output "$EXTERNAL" --off
        qtile cmd-obj -o cmd -f reconfigure_screens
        notify-send "Display" "Solo pantalla interna"
        ;;
    "Solo externa")
        xrandr --output "$EXTERNAL" --auto --output "$PRIMARY" --off
        qtile cmd-obj -o cmd -f reconfigure_screens
        notify-send "Display" "Solo pantalla externa"
        ;;
    "Espejo")
        xrandr --output "$EXTERNAL" --auto --same-as "$PRIMARY"
        qtile cmd-obj -o cmd -f reconfigure_screens
        notify-send "Display" "Pantalla espejo"
        ;;
    "Extendida derecha")
        xrandr --output "$EXTERNAL" --auto --right-of "$PRIMARY"
        qtile cmd-obj -o cmd -f reconfigure_screens
        notify-send "Display" "Extendida a la derecha"
        ;;
    "Extendida izquierda")
        xrandr --output "$EXTERNAL" --auto --left-of "$PRIMARY"
        qtile cmd-obj -o cmd -f reconfigure_screens
        notify-send "Display" "Extendida a la izquierda"
        ;;
    "Extendida arriba")
        xrandr --output "$EXTERNAL" --auto --above "$PRIMARY"
        qtile cmd-obj -o cmd -f reconfigure_screens
        notify-send "Display" "Extendida arriba"
        ;;
    "Extendida abajo")
        xrandr --output "$EXTERNAL" --auto --below "$PRIMARY"
        qtile cmd-obj -o cmd -f reconfigure_screens
        notify-send "Display" "Extendida abajo"
        ;;
    *)
        notify-send "Display" "Opción no válida"
        ;;
esac