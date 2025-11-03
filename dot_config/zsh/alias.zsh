# Aliases

# Replace ls with eza. Sort directories first. Show git status. Show dotfiles. Use ISO for timestamps.
alias ls='eza --icons --group-directories-first --git -a --time-style long-iso'
alias ll='ls -l' # Display extended file metadata as a table.
alias lk='ls -l --sort size' # Sort by file size, largest last.
alias lt='ls -l --sort date' # Sort by modification time, newest last.
alias lx='ls -l --sort extension' # Sort by extension.

# Replace cat with bat.
alias cat='bat'

# Replace du with dust.
alias du='dust'

# Generic alias for the "fetch" application used in the dotfiles.
alias fetch='fastfetch'

# Replace grep with ripgrep (rg).
alias grep='rg'

# Replace top with btop.
alias top='btop'

# Display an image on the terminal.
alias icat='kitty +kitten icat'

# Open a file or URL in the preferred application.
alias open='xdg-open'

# Convert flac to mp3 and copy them all to the parameter path.
alias flac2mp3='fd -t f -e flac -x ffmpeg -i "{}" -qscale:a 0 "{.}.mp3" && fd -t f -e mp3 -x mv -n --debug "{.}.mp3"'

# Common mistypes.
alias cd..='cd ..'
