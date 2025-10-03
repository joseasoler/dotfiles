# Dotfiles

[Arch Linux](https://archlinux.org/) managed using [chezmoi](https://github.com/twpayne/chezmoi). This repository may contain files from other sources. In that case, each one of them will have its own LICENSE file. All other content is under the [UNLICENSE](UNLICENSE).

## System

* AMD [Zen 5 CPU](https://en.wikipedia.org/wiki/Zen_5)
* AMD [RDNA 4 GPU](https://en.wikipedia.org/wiki/RDNA_4)
* [Arch Linux](https://archlinux.org/)
* [KDE](https://wiki.archlinux.org/title/KDE)
* [multilib](https://wiki.archlinux.org/title/Official_repositories#multilib) support
* Windows dual boot.

## System Setup

### BIOS

* Disable Secure Boot.

* Other common optimization steps such as enabling rebar, XMP, PBO and so on.

### Windows

* Install Windows using all space on the hard drive.

* Update Windows.

* Defragment the Windows partition.

* Disable hibernation and set system time to UTC. In a Windows command-line shell with administrator privileges:

```bat
powercfg /H off
reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation" /v RealTimeIsUniversal /d 1 /t REG_DWORD /f
```

### Arch Linux

Follow the Arch Linux [Installation Guide](https://wiki.archlinux.org/title/Installation_guide). This README contains specific choices to take at specific points of the official guide.

#### Partitions

* /boot partition, mounted at /mnt/boot. 1 GiB, "Linux extended boot" (XBOOTLDR). FAT32.

* [SWAP] partition of the minimum recommended size, 4GiB.

* / partition, mounted at /mnt.

* The existing Windows EFI partition can be reused. Mount at /mnt/efi.

#### Install essential packages

Install the base system, [boot loader](https://wiki.archlinux.org/title/Arch_boot_process#Boot_loader) and network packages.

```bash
pacstrap -K /mnt base base-devel linux linux-firmware amd-ucode nano grub efibootmgr os-prober wireless_tools networkmanager man-db
```

#### Boot Loader

Follow the [GRUB](https://wiki.archlinux.org/title/GRUB) page. The instructions below are a reminder.

```bash
# Uncomment the GRUB_DISABLE_OS_PROBER=false line.
nano /etc/default/grub
grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB
grub-mkconfig -o /boot/grub/grub.cfg
```

#### Post-installation

* Enable, configure and test [NetworkManager](https://wiki.archlinux.org/title/NetworkManager).

* [Create a new user](https://wiki.archlinux.org/title/Users_and_groups#Example_adding_a_user) with [sudo permissions](https://wiki.archlinux.org/title/Sudo#Example_entries) and log in with it.

* Enable [time sync](https://wiki.archlinux.org/title/Systemd-timesyncd):

```bash
sudo systemctl enable --now systemd-timesyncd.service
```

#### Repositories

* [Enable multilib](https://wiki.archlinux.org/title/Official_repositories#Enabling_multilib).

#### Reflector

```bash
sudo pacman -Syu reflector
sudo nano /etc/xdg/reflector/reflector.conf
```

Uncomment the country line and set it to:

```bash
--country ES,FR,DE,GB
```

Then enable the service:

```bash
sudo systemctl enable --now reflector.service
```

#### DNS over HTTPS

```bash
sudo pacman -Syu dns-over-https
sudo systemctl enable --now doh-client.service
```

Follow the [Arch Linux NetworkManager wiki page](https://wiki.archlinux.org/title/NetworkManager#Setting_custom_global_DNS_servers) instructions for setting a custom global DNS server pointing to localhost.

#### makepkg

Configure [makepkg](https://wiki.archlinux.org/title/makepkg) to reduce compile times and optimize binaries. Flags taken from [ALPH flags](https://somegit.dev/ALHP/ALHP.GO/src/branch/main/flags.yaml). Check that they are up to date.

```bash
sudo nano /etc/makepkg.conf
```

CFLAGS:
* Remove `-mtune=generic`.
* Change `-O2` to `-O3`.
* Set `march` to `native`.

MAKEFLAGS:
* Uncomment and replace with `MAKEFLAGS="--jobs=$(nproc)"`.

```bash
sudo nano /etc/makepkg.conf.d/rust.conf
```

RUSTFLAGS:
* Add `-C target-cpu=native`.
* Add `-C opt-level=3`.

#### git

```bash
git config --global user.name 'Full Name'
git config --global user.email "your.email@example.ex"
git config --global init.defaultBranch main
git config --global pull.rebase true
git config --global rebase.autoStash true
git config --global merge.ff false
git config --global core.commentChar '>'
git config --global core.editor 'nano'
git config --global color.ui true
```

#### paru

[paru](https://github.com/Morganamilo/paru) is the [pacman wrapper](https://wiki.archlinux.org/title/AUR_helpers#Pacman_wrappers) used by these dotfiles.

```bash
sudo pacman -Syu git rust
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
cd ..
rm -rf paru
```

#### Audio

```bash
sudo pacman -Syu pipewire lib32-pipewire
```

#### Fonts

```bash
sudo pacman -Syu noto-fonts noto-fonts-emoji ttf-noto-nerd
```

#### KDE Plasma

```bash
sudo pacman -Syu plasma-desktop kscreen breeze-gtk kde-gtk-config xdg-desktop-portal-kde plasma-nm plasma-pa gwenview qt6-imageformats kimageformats kcolorchooser dolphin spectacle kate markdownpart konsole
```

* Launch KDE from TTY for now.

* Add keyboard layout.

* Disable sleep in power management.

* Do not warn before reboot/shutdown.

* Sound > Configure Volume Controls > Disable Play audio feedback for changes

#### SDDM

```bash
sudo pacman -Syu sddm sddm-kcm qt5-declarative
sudo systemctl enable sddm.service
```

Reboot and test. After logging in, set the SDDM theme to breeze.

#### Firefox

```bash
sudo pacman -Syu firefox
```

In `about:config`:
* Set widget.use-xdg-desktop-portal.file-picker to 1.
* Set geo.enabled to false.
* Set privacy.query_stripping.enabled and privacy.query_stripping.enabled.pbmode to true.

In `about:preferences`:
* Search for telemetry and disable all options.
* Search > Disable Show search suggestions.
* Privacy and Security > Enhanced Tracking Protection > Strict.
* Privacy and Security > Website Privacy Preferences > Tell websites not to sell or share my data.

Install uBlock Origin (or log in to Firefox Sync if you already have this plugin). In its options:

* Filter lists > Cookie Notices > Enable all.
* Filter lists > Privacy > AdGuard URL tracking protection
* Click on update now.

#### Discord

```bash
sudo pacman -Syu discord
```

* Launch discord so it will ask about KWallet. Set KWallet to blowfish and use the same password as the account password. SDDM is already set up to load KWallet automatically on login from now on.

* Add discord to KDE auto start applications.

#### Steam

```bash
sudo pacman -Syu steam vulkan-radeon lib32-vulkan-radeon
```

#### Dropbox

```bash
paru -Syu dropbox
sudo pacman -Syu dolphin-plugins libappindicator-gtk3
```

#### Audacious

```bash
sudo pacman -Syu audacious
```

* Settings > Audio > Pipewire output
* Settings > Playlist > Disable pause instead of resuming immediately
* Plugins > Status icon > Enable and close to window tray
* Add the line `"SKIP_HOST_UPDATE": true` to ~/.config/discord/settings.json

#### Libreoffice

Replace spell checker languages with the ones you need.

```bash
sudo pacman -Syu libreoffice-fresh hunspell hunspell-en_gb hunspell-es_es
```

* Launch Libreoffice.
* Tools > Options > Languages and Locales > General > Default Languages for Documents > Western > English (UK)
* Tools > Options > Languages and Locales > Writing Aids > Hunspell SpellChecker enabled.

#### vscode

```bash
sudo pacman -Syu clang code
```

Install these extensions: clangd, {LLVM}, cmake-tools {Microsoft}, C/C++ Debug (gdb) {KylinIdeTeam}.

* Set CMake: Copy Compile Commands to ${workspaceFolder}/compile_commands.json

#### pkgstats

```bash
sudo pacman -Syu pkgstats
```

## Dotfiles setup

### Private key

Required for write access to the dotfiles repo.

```bash
sudo pacman -Syu openssh
ssh-keygen -t ed25519 -C "your.email@example.ex"
```

Upload your public key to your repo hosting.

### Dotfiles installation

Replace the URL with your repo if necessary.

```bash
sudo pacman -Syu bat less btop rocm-smi-lib chezmoi eza fd ffmpeg ncdu ripgrep zsh zsh-autosuggestions zsh-syntax-highlighting starship fastfetch
chsh -s /usr/bin/zsh
chezmoi init --apply --verbose git@github.com:joseasoler/dotfiles.git
git config --global pager.log 'bat -p -l gitlog'
git config --global pager.diff 'bat'
systemctl reboot
```
