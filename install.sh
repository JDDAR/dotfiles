#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE} Installing dotfiles...${NC}"

# Create config directory if it doesn't exist
mkdir -p ~/.config

# Function to backup and link
backup_and_link() {
    local source_path=$1
    local target_path=$2
    local name=$3
    
    if [ -e "$target_path" ]; then
        echo -e "${YELLOW}⚠️  Backing up existing $name configuration...${NC}"
        mv "$target_path" "$target_path.backup.$(date +%Y%m%d_%H%M%S)"
    fi
    
    echo -e "${GREEN}🔗 Linking $name configuration...${NC}"
    ln -sf "$source_path" "$target_path"
}

# Get the directory where this script is located
DOTFILES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Link configurations
if [ -d "$DOTFILES_DIR/qtile" ]; then
    backup_and_link "$DOTFILES_DIR/qtile" "$HOME/.config/qtile" "qtile"
fi

if [ -d "$DOTFILES_DIR/rofi" ]; then
    backup_and_link "$DOTFILES_DIR/rofi" "$HOME/.config/rofi" "rofi"
fi

echo -e "${GREEN}✅ Dotfiles installed successfully!${NC}"
echo -e "${BLUE}📝 To reload qtile: Mod + Ctrl + r${NC}"
echo -e "${YELLOW}⚠️  Your old configs were backed up with timestamp${NC}"