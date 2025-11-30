from decman import Module, sh
import variables

class NordVPN(Module):
    def __init__(self, enabled):
        super().__init__(name='NordVPN', enabled=enabled, version=1.00)

    def pacman_packages(self) -> list[str]:
        packages = [
        ]

        return packages

    def aur_packages(self) -> list[str]:
        return [
            "nordvpn-bin",
        ]

    def on_enable(self):
        # sh("groupadd nordvpn")
        sh(f"sudo usermod -aG nordvpn {variables.username}")

    # def on_disable(self):
    #     sh("groupdel nordvpn")

    def systemd_units(self) -> list[str]:
        return ["nordvpnd.service"]
