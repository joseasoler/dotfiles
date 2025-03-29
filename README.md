# Dotfiles

Dotfiles for [Archlinux](https://archlinux.org/), managed using [chezmoi](https://github.com/twpayne/chezmoi).

This repository contains plugins and themes obtained from other sources. Each one of these are stored in their own folder and contain a LICENSE or LICENSE.md file that is applied to all files contained in the folder and its subfolders. Other files may contain the license info in their headers. For anything else, check [UNLICENSE](UNLICENSE).

These files assume an AMD CPU and a NVIDIA GPU.

## Operative system installation

These notes are not required for installing the dotfiles. They are reminders about how I usually install the OS.

### Windows

In a Windows command-line shell with administrator privileges:

```bat
powercfg /H off
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation" /v RealTimeIsUniversal /d 1 /t REG_DWORD /f
```

### Archlinux

#### Installation

##### Partition setup

Separate /boot partition of type "Linux extended boot" (XBOOTLDR), filesystem fat32, 4GB to be on the safe side.

##### Pacstrap packages

```bash
pacstrap -K /mnt base linux linux-firmware amd-ucode nano base-devel grub os-prober efibootmgr dhcpcd reflector
```

#### Post-installation

```bash
sudo systemctl enable –now systemd-timesyncd.service
```

Configure reflector and enable its service.

## Dotfiles installation

These instructions assume a finished Archlinux installation. 

### makepkg

Configure [makepkg](https://wiki.archlinux.org/title/makepkg) for optimizing compile times and building optimized binaries before building any packages from the AUR:

```bash
sudo nano /etc/makepkg.conf
```

Set CFLAGS, CXXFLAGS and RUSTFLAGS for [building optimized binaries](https://wiki.archlinux.org/title/makepkg#Building_optimized_binaries).
Set MAKEFLAGS for [improving compile times](https://wiki.archlinux.org/title/makepkg#Improving_compile_times).

### paru

[paru](https://github.com/Morganamilo/paru) is the [pacman wrapper](https://wiki.archlinux.org/title/AUR_helpers#Pacman_wrappers) used by these dotfiles.

```bash
sudo pacman -Syu git rust
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
cd ..
rm -r paru
```

### Setup private key

This is not needed if you plan to use a read-only checkout of this repo, only if you have a fork of this repo or are the owner.

```bash
paru -Syu openssh
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Then upload your public key to GitHub.

### Installation

Replace the `wget` and `chezmoi` URLs with your repo if necessary. The `localectl` command assumes a Spanish keyboard, replace as necessary.

```bash
paru -Syu wget
wget https://raw.githubusercontent.com/joseasoler/dotfiles/refs/heads/master/packages.txt
paru -Syu - < packages.txt
chsh -s /usr/bin/zsh
sudo systemctl enable sddm.service
chezmoi init --apply --verbose git@github.com:joseasoler/dotfiles.git
sudo localectl --no-convert set-x11-keymap es
systemctl reboot
```

## Post-installation

### .gitconfig

Remember to set the email and name values correctly.

```bash
git config –global init.defaultBranch main
```
