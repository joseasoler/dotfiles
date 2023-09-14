# Aliases

# Use eza instead of ls. Sort directories first. Show git status. Show dotfiles. Use ISO for timestamps.
alias ls='eza --icons --group-directories-first --git -a --time-style long-iso'
alias ll='ls -l' # Display extended file metadata as a table.
alias lk='ll --sort size' # Sort by file size, largest last.
alias lt='ll --sort date' # Sort by modification time, newest last.
alias lx='ll --sort extension' # Sort by extension.

# Use bat instead of cat
alias cat='bat --theme Nord'

# Use ripgrep (rg) instead of grep.
alias grep='rg'

# Other aliases.
alias open='xdg-open' # Open a file or URL in the preferred application.
alias top='btop'
alias icat='kitty +kitten icat'

# Common mistypes.
alias cd..='cd ..'

# RimWorld mod development aliases.
alias modsrim='cd /home/joseasoler/.steam/steam/steamapps/common/RimWorld/Mods'
alias workshoprim='cd /home/joseasoler/.steam/steam/steamapps/workshop/content/294100'

# Valheim mod development aliases.
alias valhmods='cd /home/joseasoler/.steam/steam/steamapps/common/Valheim/'
