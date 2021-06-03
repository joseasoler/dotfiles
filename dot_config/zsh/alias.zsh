# Aliases

# Use exa instead of ls. Sort directories first. Show git status. Show dotfiles. Use ISO for timestamps.
alias ls='exa --icons --group-directories-first --git -a --time-style long-iso'
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
alias top='bpytop'

# Common mistypes.
alias cd..='cd ..'
