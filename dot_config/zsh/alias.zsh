# Aliases

# Replace ls with eza. Sort directories first. Show git status. Show dotfiles. Use ISO for timestamps.
alias ls='eza --icons --group-directories-first --git -a --time-style long-iso'
alias ll='eza -l' # Display extended file metadata as a table.
alias lk='eza -l --sort size' # Sort by file size, largest last.
alias lt='eza -l --sort date' # Sort by modification time, newest last.
alias lx='eza -l --sort extension' # Sort by extension.

# Replace cat with bat.
alias cat='bat --theme Nord'

# Replace du with ncdu.
alias du='ncdu --color dark'

# Replace grep with ripgrep (rg).
alias grep='rg'

# Replace top with btop.
alias top='btop'

# Other aliases.
alias icat='kitty +kitten icat'
alias open='xdg-open' # Open a file or URL in the preferred application.

# Common mistypes.
alias cd..='cd ..'
