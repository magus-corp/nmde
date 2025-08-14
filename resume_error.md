Of course. It's frustrating to circle back to the original error, but it means we've successfully eliminated all other possibilities. We now know exactly where the problem is, even if we don't know *why*.

Here is a detailed summary of our entire debugging process. You can use this to ask for help on a forum (like the Arch Linux or Hyprland forums), in a Discord server, or in a bug report to the `nmde`/`seamless-login` developer. It provides all the context and evidence needed for an expert to help you.

-----

### **Subject: Debugging Boot Failure: `seamless-login` script fails with "unsupported extension conf" error**

#### **System Information**

  * **OS:** [Your Linux Distribution, e.g., Arch Linux, EndeavourOS]
  * **Window Manager/Compositor:** Hyprland
  * **Login Method:** Custom `systemd` service (`nmde-seamless-login.service`) designed for a seamless, TTY-based auto-login.

#### **1. Summary of the Problem**

When the `nmde-seamless-login.service` is enabled, the system fails to boot into the Hyprland graphical session on TTY1. The service enters a restart loop, and the screen may flash or get stuck. The system remains accessible via SSH or by switching to another TTY (e.g., `Ctrl+Alt+F2`), from which a graphical session can sometimes be started manually. The goal is to fix the automatic login service.

#### **2. Debugging Steps and Findings**

We have systematically isolated the problem through the following steps:

  * **Initial Analysis:** The command `systemctl status nmde-seamless-login.service` showed the service was in a "crash loop" (`Active: activating (auto-restart)`), with the main process exiting with `status=1/FAILURE`.

  * **Initial Error Message:** The first clue appeared in the system journal (`journalctl`):

    ```
    seamless-login[PID]: Trying to remove unit with unsupported extension conf
    ```

    We confirmed this message comes directly from the `seamless-login` process, not from `systemd` itself.

  * **Investigation 1: Ruled out misnamed `systemd` unit files.**

      * **Action:** We performed a recursive search for any `.conf` files in the systemd directory: `find /etc/systemd -type f -name "*.conf"`.
      * **Result:** The search only returned standard system configuration files (e.g., `logind.conf`, `journald.conf`) and valid "drop-in" configurations in `.service.d` directories. No custom, misnamed service files were found.
      * **Conclusion:** The error is not caused by a file like `myservice.conf` in `/etc/systemd/system`.

  * **Investigation 2: Ruled out interference from user services.**

      * **Action:** We discovered and temporarily disabled a custom user timer (`organize-files.timer`) located in `~/.config/systemd/user/` using `systemctl --user disable`.
      * **Result:** Disabling this user service had no effect on the boot failure.
      * **Conclusion:** The problem is not caused by other user-level services.

  * **Investigation 3: Ruled out manual execution.**

      * **Action:** We attempted to run the service's `ExecStart` command directly from a TTY shell.
      * **Result 1 (as user):** `Failed to open VT: Permission denied`. This is expected, as a regular user cannot control the VT.
      * **Result 2 (with `sudo`):** `DBus.Error.NotSupported...`. This is also expected, as running a graphical session with `sudo` breaks the user's D-Bus session.
      * **Conclusion:** The `seamless-login` script requires the specific permissions and environment provided by `systemd` and cannot be debugged by running it manually.

  * **Investigation 4: Captured the script's direct output.**

      * **Action:** To capture the true error, we created a wrapper script and modified the service to execute it. This script redirected all output (`stdout` and `stderr`) from the `seamless-login` command to a log file.
      * **Result:** After rebooting, the log file (`/home/cmgus/hyprland_log.txt`) was created and contained only one line:
        ```
        Trying to remove unit with unsupported extension conf
        ```
      * **Conclusion:** We have definitively proven that this confusing error message is the only output produced by the `seamless-login` script before it fails.

#### **3. Relevant Files**

  * **Service File (`/etc/systemd/system/nmde-seamless-login.service`):**
    ```ini
    [Unit]
    Description=nmde Seamless Auto-Login
    Documentation=https://github.com/magus-corp/nmde
    Conflicts=getty@tty1.service
    After=systemd-user-sessions.service getty@tty1.service plymouth-quit.service systemd-logind.service
    PartOf=graphical.target

    [Service]
    Type=simple
    ExecStart=/usr/local/bin/seamless-login uwsm start -- hyprland.desktop
    Restart=always
    RestartSec=2
    User=cmgus
    TTYPath=/dev/tty1
    TTYReset=yes
    TTYVHangup=yes
    TTYVTDisallocate=yes
    StandardInput=tty
    StandardOutput=journal
    StandardError=journal+console
    PAMName=login

    [Install]
    WantedBy=graphical.target
    ```

#### **4. Core Unanswered Question**

We have confirmed the `nmde-seamless-login.service` fails because the `/usr/local/bin/seamless-login` executable exits with an error. All attempts to debug have led back to the same cryptic message: **`Trying to remove unit with unsupported extension conf`**.

The fundamental question is: **What file is the `seamless-login` script trying to find or process that is causing this specific error?** Since it's not in `/etc/systemd/`, it must be a configuration file related to `seamless-login` or `Hyprland` located elsewhere on the system.
