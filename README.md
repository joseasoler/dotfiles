# Dotfiles

Dotfiles for [Archlinux](https://archlinux.org/), managed using [chezmoi](https://github.com/twpayne/chezmoi).

This repository contains plugins and themes obtained from other sources. Each one of these are stored in their own folder and contain a LICENSE or LICENSE.md file that is applied to all files contained in the folder and its subfolders. Other files may contain the license info in their headers. For anything else, check [UNLICENSE](UNLICENSE).

## Installation

This section contains instructions for installing the dependencies of these dotfiles, along with other useful configuration steps. These instructions assume a finished Archlinux installation. 

### makepkg configuration

Configure [makepkg](https://wiki.archlinux.org/title/makepkg) for optimizing compile times and building optimized binaries before building any packages from the AUR:

```bash
sudo nano /etc/makepkg.conf
```

Set CFLAGS, CXXFLAGS and RUSTFLAGS for [building optimized binaries](https://wiki.archlinux.org/title/makepkg#Building_optimized_binaries).
Set MAKEFLAGS for [improving compile times](https://wiki.archlinux.org/title/makepkg#Improving_compile_times).

### paru

[paru](https://github.com/Morganamilo/paru) is the [pacman wrapper](https://wiki.archlinux.org/title/AUR_helpers#Pacman_wrappers) used by these dotfiles.

```bash
sudo pacman -S git rust
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
cd ..
rm -r paru
```

### Installation

```bash
paru -S - < packages.txt
chsh -s /usr/bin/zsh
sudo systemctl enable sddm.service
chezmoi init --apply --verbose git@github.com:joseasoler/dotfiles.git
sudo reboot
```

## Post-installation

### .gitconfig

Remember to set the email and name values correctly.

### Keyboard layout

```bash
sudo localectl --no-convert set-x11-keymap es
sudo reboot
```
