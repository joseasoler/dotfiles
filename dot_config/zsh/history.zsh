# https://www.soberkoder.com/better-zsh-history/
# http://zsh.sourceforge.net/Doc/Release/Options.html#History

HISTFILE=~/.zsh_history
HISTSIZE=2000000 # Number of commands that are loaded into memory from the history file.
SAVEHIST=1000000 # Number of commands that are stored in the zsh history file.

setopt INC_APPEND_HISTORY # Append new entries immediately.
setopt HIST_IGNORE_ALL_DUPS # When an entry is added, remove all previous identical entries.
setopt HIST_NO_STORE # Remove the history command fc -l from history.
setopt HIST_REDUCE_BLANKS # Remove superfluous blanks from each entry being added.
