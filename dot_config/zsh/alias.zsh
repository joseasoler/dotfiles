# Aliases

# ls aliases.
alias ls='colorls --sd --gs -A' # Use colorls. Sort directories first. Show git status. Do not list . and ..
alias lk='ls -lSr' # Sort by file size, largest last.
alias lt='ls -ltr' # Sort by modification time, newest last.
alias lx='ls -lX' # Sort by file extension.

# Other aliases.
alias open='xdg-open' # Open a file or URL in the preferred application.
alias top='bpytop'

# Common mistypes.
alias cd..='cd ..'
