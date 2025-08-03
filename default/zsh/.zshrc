# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="powerlevel10k/powerlevel10k"

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to disable biweekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often auto-updates happen:
# zstyle ':omz:update'
# frequency 13

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set it to "mm/dd/yyyy" (default) or "dd.mm.yyyy"
# HIST_STAMPS="dd.mm.yyyy"

# Uncomment the following line if you don't like Oh My Zsh's auto-completion.
# DISABLE_AUTO_UPDATE="true"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(git pcre-utils zsh-navigation-tools)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh

# User configuration
# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your terminal emulator's font to a Powerline-compatible font.
# For example, in Alacritty, you might add:
# font:
#   normal:
#     family: 'Hack Nerd Font'
#   size: 10

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# Custom additions for this project
if [ -f "$HOME/.magus_alias" ]; then
  source "$HOME/.magus_alias"
fi

if [ -f "$HOME/.profile" ]; then
  source "$HOME/.profile"
fi

# Set a default editor if not already set
export EDITOR="${EDITOR:-nvim}"
