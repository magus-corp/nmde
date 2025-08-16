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

## Installation Flow

Here is a visual representation of the `install.sh` script's execution flow. The main script orchestrates a series of stages, with each stage sourcing scripts from specific directories to perform its tasks.

```mermaid
graph TD
    A[install.sh] --> B[Position-Independent Setup];
    B --> C[Stage 1: Preflight];
    C --> D[Stage 2: Configuration];
    D --> E[Stage 3: Development];
    E --> F[Stage 4: Plymouth Logo];
    F --> G[Stage 5: Desktop];
    G --> H[Stage 6: Apps];
    H --> I[Stage 7: System Updates];
    I --> J[Stage 8: Reboot];

    subgraph "Preflight (install/preflight)"
        C --- C1[aur.sh];
        C --- C2[presentation.sh];
    end

    subgraph "Configuration (install/config)"
        D --- D1[identification.sh];
        D --- D2[config.sh];
        D --- D3[detect-keyboard-layout.sh];
        D --- D4[fix-fkeys.sh];
        D --- D5[network.sh];
        D --- D6[power.sh];
        D --- D7[timezones.sh];
        D --- D8[login.sh];
        D --- D9[nvidia.sh];
    end

    subgraph "Development (install/development)"
        E --- E1[terminal.sh];
        E --- E2[development.sh];
        E --- E3[nvim.sh];
        E --- E4[ruby.sh];
        E --- E5[docker.sh];
        E --- E6[firewall.sh];
        E --- E7[zsh.sh];
    end

    subgraph "Plymouth Logo (bin)"
        F --- F1[nmde-generate-logo];
    end

    subgraph "Desktop (install/desktop)"
        G --- G1[desktop.sh];
        G --- G2[hyprlandia.sh];
        G --- G3[theme.sh];
        G --- G4[bluetooth.sh];
        G --- G5[asdcontrol.sh];
        G --- G6[fonts.sh];
        G --- G7[printer.sh];
    end

    subgraph "Apps (install/apps)"
        H --- H1[webapps.sh];
        H --- H2[xtras.sh];
        H --- H3[mimetypes.sh];
    end
```
