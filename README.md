# Dotfiles

Dotfiles for [Archlinux](https://archlinux.org/), managed using [chezmoi](https://github.com/twpayne/chezmoi)

This repository contains plugins and themes obtained from other sources. Each one of these are stored in their own folder and contain a LICENSE or LICENSE.md file that is applied to all files contained in the folder and its subfolders. Other files may contain the license info in their headers. For anything else, check [UNLICENSE](UNLICENSE).

## Installation

```bash
sudo pacman -S git
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
cd ..
rm -r paru
paru -S sddm i3-gaps ttf-inconsolata ttf-dejavu nerd-fonts-meslo i3lock perl-json-xs perl-anyevent-i3 dunst i3-volume rofi flameshot feh playerctl xcb-util-xrm cava arandr sox pavucontrol i3blocks pacman-contrib acpi lm_sensors gsimplecal lxappearance kvantum-qt5 xorg-xrdb spicetify-cli kvantum-theme-nordic-git nordic-theme-git papirus-icon-theme zsh zsh-autosuggestions zsh-syntax-highlighting zsh-theme-powerlevel10k exa man-db man-pages neofetch xdg-utils peco-bin kolourpaint bpytop ttf-ubraille network-manager-applet thunar tumbler gvfs featherpad firefox diff-so-fancy gwe kitty pulseaudio chezmoi spotify bat fd ripgrep tokei
sudo systemctl enable sddm.service
chezmoi init --apply --verbose git@github.com:joseasoler/dotfiles.git
sudo reboot
```

### Post-installation

#### Keyboard layout

```bash
sudo localectl --no-convert set-x11-keymap es
```

#### Spotify

```bash
# Launch spotify at least once
spotify
sudo chmod a+wr /opt/spotify
sudo chmod a+wr /opt/spotify/Apps -R
spicetify backup apply enable-devtool
```
