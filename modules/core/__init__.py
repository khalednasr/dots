from decman import Module, File, sh
import variables
import textwrap

class Core(Module):
    def __init__(self, enabled, cpu="amd"):
        super().__init__(name='Core', enabled=enabled, version=1.0)
        self.cpu = cpu

    def pacman_packages(self) -> list[str]:
        return [
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

    def aur_packages(self) -> list[str]:
        return [
            "decman",
            "yay-bin",
        ]

    def files(self) -> dict[str, File]:
        return {
            f"/home/{variables.username}/.gitconfig": File(
                content = textwrap.dedent(f'''
                [user]
                    name = {variables.git_username}
                    email = {variables.git_email}
                [init]
                    defaultBranch = main
                '''),
                owner = variables.username
                )
        }
