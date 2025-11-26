from decman import Module, File
import variables
import textwrap

class Desktop(Module):
    def __init__(self, enabled, laptop=False):
        super().__init__(name='Core', enabled=enabled, version=1.01)
        self.laptop = laptop

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
            # "polkit-gnome",

            # DMS optional depedencies
            "qt6-multimedia",
            "qt6-multimedia-gstreamer",
            "matugen",
            "cava",

            # Terminal
            "kitty",

            # Browser
            "firefox",

            # Fonts
            "noto-fonts",

            # Utilities
            "udiskie"
        ]

        if self.laptop:
            packages += [
                "brightnessctl",
                "power-profiles-daemon",
            ]

        return packages

    def aur_packages(self) -> list[str]:
        return [
            # DMS and optional dependencies
            "dms-shell-bin",
            "dgop-bin",
            "dsearch-bin",
        ]

    def files(self) -> dict[str, File]:
        return {
            # Niri config
            f"{variables.config_dir}/niri/config.kdl":
                File(source_file="./modules/desktop/config/niri/config.kdl", owner=variables.username),

            # Kitty config
            f"{variables.config_dir}/kitty/kitty.conf": File(
                content=textwrap.dedent('''
                    include dank-tabs.conf
                    include dank-theme.conf
                '''),
                owner=variables.username
            ),
        }

    def systemd_units(self) -> list[str]:
        return ["ly.service"]
