from decman import Module, File
import variables
import textwrap

class Core(Module):
    def __init__(self, enabled, cpu="amd", gpus=[]):
        super().__init__(name='Core', enabled=enabled, version=1.0)
        self.cpu = cpu
        self.gpus = gpus

    def pacman_packages(self) -> list[str]:
        packages = [
            f"{self.cpu}-ucode",
            "base",
            "base-devel",
            "efibootmgr",
            "linux",
            "linux-firmware",
            "networkmanager",
            "zram-generator",
            "git",
            "github-cli",
            "yazi",
            "less",
        ]

        if "nvidia" in self.gpus:
            packages += ["nvidia-open", "nvidia-settings"]

        return packages

    def aur_packages(self) -> list[str]:
        return [
            "decman",
            "yay-bin",
        ]

    def files(self) -> dict[str, File]:
        return {
            f"/home/{variables.username}/.gitconfig": File(
                content=textwrap.dedent(f'''
                [user]
                    name = {variables.git_username}
                    email = {variables.git_email}
                [init]
                    defaultBranch = main
                '''),
                owner=variables.username
            )
        }
