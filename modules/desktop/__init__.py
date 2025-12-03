from decman import Module, File, sh
import variables
import textwrap
import os

class Desktop(Module):
    def __init__(self, enabled):
        super().__init__(name='Core', enabled=enabled, version=1.01)

    def pacman_packages(self) -> list[str]:
        packages = [
            # Display manager
            "ly",

            # Niri and its optional dependencies
            "niri",
            "xwayland-satellite",
            "xdg-desktop-portal-gtk",
            "wl-clipboard",
            "cliphist",
            "pipewire",
            "pipewire-jack",
            "polkit-gnome",

            # DMS optional depedencies
            "qt6-multimedia",
            "qt6-multimedia-gstreamer",
            "matugen",
            "cava",
            "adw-gtk-theme",

            # Terminal
            "kitty",

            # Browsers
            "firefox",
            "qutebrowser",

            # Fonts
            "ttf-0xproto-nerd",
            "ttf-dejavu",
            "ttf-liberation",

            # Bluetooth.
            "bluez",
            "bluez-utils",
            "bluez-deprecated-tools",


            # Utilities
            "udiskie",
            "gnome-disk-utility",
        ]

        if variables.gaming:
            packages += [
                "steam"
            ]

        if variables.laptop:
            packages += [
                "brightnessctl",
                "power-profiles-daemon",
            ]

        return packages

    def aur_packages(self) -> list[str]:
        return [
            # DMS and optional dependencies
            "dms-shell-bin",
            "qt6ct-kde",  # QT theming

            # Cursor themes
            "bibata-cursor-theme-bin",

            # Firefox stuff
            "python-pywalfox",
            "firefox-tridactyl-native",
        ]

    def files(self) -> dict[str, File]:
        # Firefox theming with DMS
        home = variables.home_dir
        if os.path.exists(f"{home}/.cache/wal/dank-pywalfox.json"):
            sh(f"ln -sf {home}/.cache/wal/dank-pywalfox.json {home}/.cache/wal/colors.json")

        return {
            # Ly config
            "/etc/ly/config.ini":
                File(source_file="./modules/desktop/config/ly/config.ini"),

            # Niri config
            f"{variables.config_dir}/niri/config.kdl":
                File(source_file="./modules/desktop/config/niri/config.kdl", owner=variables.username),

            # Kitty config
            f"{variables.config_dir}/kitty/kitty.conf": File(
                content=textwrap.dedent('''
                    include dank-tabs.conf
                    include dank-theme.conf
                    font_family 0xProtoNerdFontMono
                    map super+shift+t launch --cwd=current --type=os-window
                '''),
                owner=variables.username),

            # GTK/DMS theming
            f"{variables.config_dir}/gtk-3.0/gtk.css": File(
                content='@import url("dank-colors.css");',
                owner=variables.username),

            f"{variables.config_dir}/gtk-4.0/gtk.css": File(
                content='@import url("dank-colors.css");',
                owner=variables.username),

            # Firefox/Tridactyl config
            f"{variables.config_dir}/tridactyl/tridactylrc":
                File(source_file="./modules/desktop/config/tridactyl/tridactylrc", owner=variables.username),
        }

    def file_variables(self) -> dict[str, str]:

        niri_display_config = ""

        for display, conf in variables.displays.items():
            niri_display_config += textwrap.dedent('''
                output "%s" {
                    mode "%s"
                    scale %s
                }
            ''' % (display, conf['mode'], conf['scale']))

        return {
            "//%NIRI_OUTPUT_CONFIGURATION%//": niri_display_config
        }

    def systemd_units(self) -> list[str]:
        return [
            "ly.service",
            "bluetooth.service",
        ]

    def on_enable(self):
        sh("rfkill unblock bluetooth")
