# NMDE: A System Configuration and Installation Project

This project provides a comprehensive set of scripts for configuring and installing a personalized development environment. It aims to automate the setup process, ensuring a consistent and efficient system.

## Features

*   **Zsh with Powerlevel10k**: Sets up Zsh as the default shell with the highly customizable Powerlevel10k theme and essential plugins (autosuggestions, syntax highlighting).
*   **Qutebrowser**: Configures Qutebrowser as the default web browser.
*   **Lowercase XDG User Directories**: Ensures standard user directories (Downloads, Documents, etc.) are created and configured in lowercase for consistency.
*   **Automated Dotfile Management**: Manages various configuration files (dotfiles) by linking or copying them to the appropriate locations.
*   **Package Management**: Handles installation of core system packages, desktop environment components, development tools, and applications.

## Installation

To install this system configuration, clone the repository and run the `boot.sh` script.

### Standard Installation

```bash
git clone https://github.com/magus/nmde.git
cd nmde
./boot.sh
```

### Bare Type Installation (Minimal)

For a minimal or "bare type" installation, you can set the `nmde_BARE` environment variable to `true`. This typically results in a faster installation by omitting certain non-essential components.

```bash
git clone https://github.com/magus/nmde.git
cd nmde
nmde_BARE=true ./boot.sh
```

Alternatively, for a quick bare install via `wget`:

```bash
wget -qO- https://raw.githubusercontent.com/magus/nmde/main/boot.sh | nmde_BARE=true bash
```

**Note:** After installation, if Zsh was set as your default shell, you may need to log out and log back in for changes to take full effect. Also, run `p10k configure` in your new Zsh terminal to customize your Powerlevel10k prompt.

## Usage and Configuration

(Further details on how to use and configure the installed environment can be added here.)

## Contributing

(Information on how to contribute to this project can be added here.)

## License

(Project licensing information can be added here.)
