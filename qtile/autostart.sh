#!/bin/sh

# Función para verificar si un proceso está corriendo
is_running() {
    pgrep -x "$1" > /dev/null
}

# Función para ejecutar un comando solo si no está corriendo
run_if_not_running() {
    if ! is_running "$1"; then
        echo "Iniciando $1..."
        $2 &
    else
        echo "$1 ya está ejecutándose"
    fi
}

# Esperar un poco para que el sistema se estabilice
sleep 2

# Matar procesos previos si existen (para evitar duplicados)
pkill picom 2>/dev/null
pkill nitrogen 2>/dev/null
pkill nm-applet 2>/dev/null

# Pequeña pausa
sleep 1

# Iniciar picom con tu configuración
echo "Iniciando picom..."
picom --config ~/.config/picom/picom.conf --daemon

# Restaurar wallpaper con nitrogen
echo "Restaurando wallpaper..."
nitrogen --restore &

# Iniciar network manager applet
echo "Iniciando nm-applet..."
nm-applet &

# Opcional: otros servicios que podrías querer
# run_if_not_running "blueman-applet" "blueman-applet"
# run_if_not_running "flameshot" "flameshot"

echo "Autostart completado"