#!/bin/bash

# Configuración del entorno
export HOME=/home/JDAAR
export PATH=$PATH:/usr/bin:/usr/local/bin

# Registrar que el script se ejecutó
echo "Script ejecutado a las $(date)" > /tmp/power_menu_debug.log

# Variables
uptime=$(uptime -p | sed -e 's/up //g')
host=$(hostname)



# Opciones del menú con iconos coloreados usando Pango markup
shutdown='󰐥'
reboot='󰕇'
logout='󰍃'
suspend='󰤄'
lock='󰌾'
yes='󰄬'
no='󰄱'

# Comando para mostrar el menú de Rofi con soporte para markup
rofi_cmd() {
    rofi -dmenu -markup-rows \
        -p "$host" \
        -mesg "Uptime: $uptime" \
        -theme ~/.config/rofi/themes/components/powerMenu/stylePowerMenu.rasi
}

# Comando para el diálogo de confirmación con soporte para markup
confirm_cmd() {
    rofi -dmenu -markup-rows \
        -p 'Confirmación' \
        -mesg '¿Estás seguro?' \
        -theme-str 'window {location: center; anchor: center; fullscreen: false; width: 250px;}' \
        -theme-str 'mainbox {children: [ "message", "listview" ];}' \
        -theme-str 'listview {columns: 2; lines: 1;}' \
        -theme-str 'element-text {horizontal-align: 0.5;}' \
        -theme-str 'textbox {horizontal-align: 0.5;}' \
        -theme ~/.config/rofi/themes/components/powerMenu/stylePowerMenu.rasi
}

# Función para pedir confirmación
confirm_exit() {
    echo -e "$yes\n$no" | confirm_cmd
}

# Función para ejecutar comandos
run_cmd() {
    selected="$(confirm_exit)"
    if [[ "$selected" == "$yes" ]]; then
        case $1 in
            --shutdown)
                systemctl poweroff
                ;;
            --reboot)
                systemctl reboot
                ;;
            --suspend)
                # Pausar multimedia y mutar audio (opcional)
                mpc -q pause 2>> /tmp/power_menu_debug.log
                amixer set Master mute 2>> /tmp/power_menu_debug.log
                systemctl suspend
                ;;
            --logout)
                qtile cmd-obj -o cmd -f shutdown
                ;;
        esac
    else
        echo "Acción cancelada" >> /tmp/power_menu_debug.log
        exit 0
    fi
}

# Mostrar el menú
chosen=$(echo -e "$lock\n$suspend\n$logout\n$reboot\n$shutdown" | rofi_cmd)

# Registrar la selección
echo "Opción seleccionada: $chosen" >> /tmp/power_menu_debug.log

# Ejecutar la acción seleccionada
case $chosen in
    "$shutdown")
        run_cmd --shutdown
        ;;
    "$reboot")
        run_cmd --reboot
        ;;
    "$suspend")
        run_cmd --suspend
        ;;
    "$logout")
        run_cmd --logout
        ;;
    "$lock")
        if [[ -x '/usr/bin/betterlockscreen' ]]; then
            betterlockscreen -l
        elif [[ -x '/usr/bin/i3lock' ]]; then
            i3lock
        else
            echo "No se encontró un programa de bloqueo" >> /tmp/power_menu_debug.log
        fi
        ;;
    *)
        echo "Opción inválida: $chosen" >> /tmp/power_menu_debug.log
        exit 1
        ;;
esac