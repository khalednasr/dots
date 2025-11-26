from decman import Module, File, sh
import variables

class Desktop(Module):
    def __init__(self, enabled, laptop=False):
        super().__init__(name='Core', enabled=enabled, version=1.0)
        self.laptop = laptop

    def pacman_packages(self) -> list[str]:
        packages = [
            "xwayland-satellite",
            "xdg-desktop-portal-gnome",
            "xdg-desktop-portal-gtk",
            "wl-clipboard",
            "pipewire",
            "pipewire-jack",
            "niri",
        ]

        if self.laptop:
            packages += [
                "brightnessctl",
            ]

        return packages

    def aur_packages(self) -> list[str]:
        return [
        ]

    def files(self) -> dict[str, File]:
        return {}
