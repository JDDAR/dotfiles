# 🚀 My Dotfiles

> Personal configuration files for my Linux setup

## 📋 Components

- **🪟 Qtile**: Tiling window manager configuration
- **🔍 Rofi**: Application launcher and dmenu replacement

## 🎯 Features

- Clean and minimal qtile configuration
- Custom keybindings for productivity
- Stylish rofi theme
- Easy installation with automated script

## 📦 Installation

### Prerequisites
```bash
# Arch Linux
sudo pacman -S qtile rofi

# Ubuntu/Debian
sudo apt install qtile rofi
```

### Quick Install
```bash
git clone https://github.com/TU-USUARIO/dotfiles.git
cd dotfiles
./install.sh
```

### Manual Install
```bash
# Backup existing configs
mv ~/.config/qtile ~/.config/qtile.backup 2>/dev/null
mv ~/.config/rofi ~/.config/rofi.backup 2>/dev/null

# Create symlinks
ln -sf $(pwd)/qtile ~/.config/qtile
ln -sf $(pwd)/rofi ~/.config/rofi
```

## 🎨 Screenshots

*Coming soon...*

## ⚙️ Key Bindings (Qtile)

| Key | Action |
|-----|--------|
| `Mod + Return` | Open terminal |
| `Mod + d` | Launch rofi |
| `Mod + q` | Close window |
| `Mod + Ctrl + r` | Reload qtile |

## 🔧 Customization

Feel free to modify the configurations to suit your needs:

- **Qtile config**: `qtile/config.py`
- **Rofi theme**: `rofi/config.rasi`

## 🤝 Contributing

Found a bug or have a suggestion? Feel free to open an issue or submit a pull request!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the qtile and rofi communities
- Inspired by the amazing dotfiles community on GitHub

---

⭐ **Star this repo if you found it helpful!**