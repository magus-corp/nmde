#!/bin/bash

yay -S --noconfirm --needed \
  cargo clang llvm mise \
  imagemagick \

# Setup Zsh and Powerlevel10k
/home/magus/projects/magus/nmde/install/development/zsh.sh

  mariadb-libs postgresql-libs \
  github-cli \
  lazygit lazydocker-bin
