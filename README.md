# NMDE: Not My Desktop Environment

NMDE is a comprehensive, automated system for setting up and managing a complete and personalized Arch Linux desktop environment. It's built around the Hyprland Wayland compositor and a curated set of modern, efficient tools. The goal of NMDE is to provide a beautiful, functional, and highly-automated development environment out of the box, while still allowing for deep personalization.

![NMDE Screenshot](https://raw.githubusercontent.com/magus-corp/nmde/main/docs/screenshot.png)

## Philosophy

- **Automation First:** From initial installation to ongoing configuration changes, NMDE strives to automate as much as possible, ensuring a consistent and reproducible environment.
- **Sensible Defaults:** NMDE comes with a set of carefully chosen defaults for applications, themes, and configurations, providing a great experience from the first boot.
- **Deep Personalization:** While highly automated, NMDE is not a black box. It's designed to be easily customized and extended. User configurations are kept separate from the core NMDE files, making updates seamless.
- **Modern & Efficient:** The environment is built with modern, fast, and keyboard-driven tools to maximize productivity.

## Features

- **Hyprland Desktop:** A fully configured desktop environment based on the Hyprland Wayland compositor, with Waybar, Hyprlock, and other essential components.
- **Complete Theming System:** Easily switch between multiple pre-configured themes that cover everything from your terminal and editor to your application launcher and system bars.
- **Automated Installation:** A single script to install and configure the entire system, including applications, development tools, and all dotfiles.
- **TUI for Management:** A simple Text-based User Interface (`nmde`) for managing your environment, including theme switching, updates, and more.
- **Migration System:** A robust migration system allows for smooth updates to your configuration over time without overwriting your personal changes.
- **Curated Application Suite:** Includes a selection of applications for development, productivity, and system management, such as Neovim (with a LazyVim starter config), Docker, Qutebrowser, and more.
- **Utility Scripts:** A collection of scripts in `~/.local/share/nmde/bin` for common tasks like taking screenshots, managing power, and changing themes.

## Installation

You can install NMDE with a single command. This will clone the repository and start the installation process.

```bash
wget -qO- https://raw.githubusercontent.com/magus-corp/nmde/main/boot.sh | bash
```

For a minimal installation that skips most applications, you can set the `nmde_BARE` environment variable:

```bash
wget -qO- https://raw.githubusercontent.com/magus-corp/nmde/main/boot.sh | nmde_BARE=true bash
```

The installation script will guide you through the process. After it's done, your system will reboot into your new NMDE environment.

## Usage

### Managing your environment

The `nmde` command provides a simple TUI for managing your environment. You can launch it from your terminal or application launcher. From there, you can:

-   **Change themes:** Select from a list of installed themes.
-   **Install new themes:** Provide a git repository URL to install a new theme.
-   **Update your system:** Run updates for NMDE, system packages, and various components.
-   **Run setup scripts:** Configure additional tools like Docker, Dropbox, and more.

### Customization

You are encouraged to customize your environment. Here are some key files and directories for personalization:

-   **Hyprland:** `~/.config/hypr/hyprland.conf` is the main entry point for your personal Hyprland configuration. You can add your own settings here, which will be loaded on top of the NMDE defaults.
-   **Shell:** `~/.zshrc` is your personal Zsh configuration file. You can add your own aliases, functions, and settings here.
-   **Themes:** To create your own theme, you can copy one of the existing themes in `~/.local/share/nmde/themes` and modify it.

### Updating

To update NMDE and your system, you can use the `nmde-update` command, or use the "Update" menu in the `nmde` TUI. This will pull the latest changes from the NMDE repository, run any pending migrations, and update your system packages.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request on the [GitHub repository](https://github.com/magus-corp/nmde).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.