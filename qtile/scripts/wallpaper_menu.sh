#!/bin/bash

# Configuración
WALLPAPER_DIR="$HOME/Imágenes/wallpaper"
ROFI_THEME="$HOME/.config/rofi/themes/components/wallpaper/wallpaper.rasi"
ROFI_THEME_ACTIONS="$HOME/.config/rofi/themes/components/wallpaper/actions.rasi"

# Verificaciones
[ -d "$WALLPAPER_DIR" ] || { notify-send "Error" "Carpeta no existe: $WALLPAPER_DIR"; exit 1; }
command -v feh >/dev/null || { notify-send "Error" "feh no está instalado"; exit 1; }
command -v rofi >/dev/null || { notify-send "Error" "rofi no está instalado"; exit 1; }

# Función para generar miniaturas uniformes (OBLIGATORIO para tamaños consistentes)
generate_thumbnails() {
    local thumb_dir="$HOME/.cache/wallpaper-thumbnails"
    mkdir -p "$thumb_dir"
    
    echo "Generando miniaturas uniformes..."
    
    find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) | while read -r img; do
        local basename=$(basename "$img")
        local thumb_path="$thumb_dir/$basename"
        
        # Generar miniatura solo si no existe o es más antigua que la original
        if [ ! -f "$thumb_path" ] || [ "$img" -nt "$thumb_path" ]; then
            # Crear miniatura cuadrada de 118x118 con crop centrado
            convert "$img" \
                -resize "118x118^" \
                -gravity center \
                -extent "118x118" \
                -quality 85 \
                "$thumb_path" 2>/dev/null
        fi
    done
    
    echo "Miniaturas generadas en: $thumb_dir"
}

# Función para mostrar menú de pantallas
show_display_menu() {
    PRIMARY=$(xrandr --query | grep " connected primary" | awk '{print $1}')
    [ -z "$PRIMARY" ] && PRIMARY=$(xrandr --query | grep " connected" | head -1 | awk '{print $1}')
    EXTERNAL=$(xrandr --query | grep " connected" | grep -v "$PRIMARY" | awk '{print $1}')
    
    if [ -z "$EXTERNAL" ]; then
        notify-send "Pantalla" "Solo pantalla principal detectada"
        return
    fi
    
    CHOICE=$(printf "%s\n" \
        "<span size='xx-large'>󰌢</span>\nSolo interna" \
        "<span size='xx-large'>󰍺</span>\nSolo externa" \
        "<span size='xx-large'>󰍹</span>\nEspejo" \
        "<span size='xx-large'>󰑮</span>\nExtendida derecha" \
        "<span size='xx-large'>󰑭</span>\nExtendida izquierda" \
        "<span size='xx-large'>󰑯</span>\nExtendida arriba" \
        "<span size='xx-large'>󰑰</span>\nExtendida abajo" | \
        rofi -dmenu -p "⚙️ Configurar pantallas" -theme "$ROFI_THEME_ACTIONS" -markup-rows)
    
    case "$CHOICE" in
        *"Solo interna"*) xrandr --output "$PRIMARY" --auto --output "$EXTERNAL" --off ;;
        *"Solo externa"*) xrandr --output "$EXTERNAL" --auto --output "$PRIMARY" --off ;;
        *"Espejo"*) xrandr --output "$EXTERNAL" --auto --same-as "$PRIMARY" ;;
        *"Extendida derecha"*) xrandr --output "$EXTERNAL" --auto --right-of "$PRIMARY" ;;
        *"Extendida izquierda"*) xrandr --output "$EXTERNAL" --auto --left-of "$PRIMARY" ;;
        *"Extendida arriba"*) xrandr --output "$EXTERNAL" --auto --above "$PRIMARY" ;;
        *"Extendida abajo"*) xrandr --output "$EXTERNAL" --auto --below "$PRIMARY" ;;
        *) return ;;
    esac
    
    qtile cmd-obj -o cmd -f reconfigure_screens
    notify-send "Pantalla" "Configuración aplicada: $CHOICE"
}

# Obtener lista de imágenes
get_images() {
    find "$WALLPAPER_DIR" -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) -printf '%P\0'
}

#menu principal 
show_action_menu() {
    CHOICE=$(
        # Usar formato de icono y texto separados
        printf "%s\0icon\x1f%s\n" \
            "Seleccionar Wallpaper" "NICE" \
            "Configurar Pantallas" "󰍹" \
            "Recargar Lista" "󰑓" \
            "Salir" "󰅙" | \
        rofi -dmenu -p "🎨 Gestión de Wallpapers" -theme "$ROFI_THEME_ACTIONS" \
             -show-icons -markup-rows
    )

    case "$CHOICE" in
        "Seleccionar Wallpaper")
            show_wallpaper_selector
            ;;
        "Configurar Pantallas")
            show_display_menu
            ;;
        "Recargar Lista")
            command -v convert >/dev/null && generate_thumbnails
            show_action_menu
            ;;
        "Salir")
            exit 0
            ;;
        *)
            exit 0
            ;;
    esac
}
# Mostrar selector de wallpapers
show_wallpaper_selector() {
    mapfile -d '' IMAGES < <(get_images)
    
    if [ ${#IMAGES[@]} -eq 0 ]; then
        notify-send "Error" "No se encontraron imágenes en $WALLPAPER_DIR"
        return
    fi
    
    # Asegurar que las miniaturas existen
    local thumb_dir="$HOME/.cache/wallpaper-thumbnails"
    
    # Mostrar wallpapers con opción de volver
    SELECTION_INDEX=$({
        # Opción para volver al menú principal
        printf "⬅️ Volver al menú principal\x00info\x1fback\n"
        
        # Mostrar todas las imágenes usando miniaturas si existen
        for img in "${IMAGES[@]}"; do
            display_name=$(basename "$img" | sed 's/\.[^.]*$//')
            local thumb_path="$thumb_dir/$(basename "$img")"
            
            # Usar miniatura si existe, sino la imagen original
            if [ -f "$thumb_path" ]; then
                printf "%s\x00icon\x1f%s\n" "$display_name" "$thumb_path"
            else
                printf "%s\x00icon\x1f%s\n" "$display_name" "$WALLPAPER_DIR/$img"
            fi
        done
    } | rofi -dmenu -show-icons -theme "$ROFI_THEME" -p "🖼️ Selecciona un wallpaper" -selected-row 1 -format i)
    
    # Si se canceló o no hay selección
    if [ -z "$SELECTION_INDEX" ]; then
        show_action_menu
        return
    fi
    
    # Si seleccionó "Volver" (índice 0)
    if [ "$SELECTION_INDEX" -eq 0 ]; then
        show_action_menu
        return
    fi
    
    # Aplicar wallpaper (usar imagen original, no miniatura)
    local wallpaper_index=$((SELECTION_INDEX - 1))
    if [ "$wallpaper_index" -ge 0 ] && [ "$wallpaper_index" -lt "${#IMAGES[@]}" ]; then
        apply_wallpaper "$WALLPAPER_DIR/${IMAGES[$wallpaper_index]}"
    fi
    
    # Volver al selector para permitir seleccionar otro
    show_wallpaper_selector
}

# Aplicar wallpaper
apply_wallpaper() {
    local wallpaper_path="$1"
    
    echo "Intentando aplicar wallpaper: $wallpaper_path"
    
    if [ -f "$wallpaper_path" ]; then
        # Intentar aplicar el wallpaper
        if feh --bg-scale "$wallpaper_path"; then
            notify-send "✅ Wallpaper" "Fondo aplicado: $(basename "$wallpaper_path")"
            echo "Wallpaper aplicado exitosamente: $wallpaper_path"
            
            # Guardar último wallpaper usado
            echo "$wallpaper_path" > "$HOME/.cache/last_wallpaper"
        else
            notify-send "❌ Error" "No se pudo aplicar el wallpaper"
            echo "Error al aplicar wallpaper: $wallpaper_path"
        fi
    else
        notify-send "❌ Error" "Archivo no encontrado: $(basename "$wallpaper_path")"
        echo "Archivo no existe: $wallpaper_path"
    fi
}

# Generar miniaturas uniformes (OBLIGATORIO para ImageMagick)
if command -v convert >/dev/null; then
    generate_thumbnails
else
    echo "ImageMagick no encontrado. Las imágenes pueden verse de diferentes tamaños."
    echo "Instala ImageMagick para miniaturas uniformes: sudo apt install imagemagick"
fi

# Iniciar con el menú de acciones
show_action_menu