from decman import Module, sh
import variables

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
            "ntfs-3g",  # for mounting windows NTFS drives
        ]

        if "nvidia" in self.gpus:
            packages += ["nvidia-open", "nvidia-settings"]

        return packages

    def aur_packages(self) -> list[str]:
        return [
            "decman",
            "yay-bin",
        ]

    def on_enable(self):
        sh(f"git config --global user.name {variables.git_username}",
           user=variables.username,
           env_overrides={"HOME": variables.home_dir})

        sh(f"git config --global user.email {variables.git_email}",
           user=variables.username,
           env_overrides={"HOME": variables.home_dir})

        sh("git config --global init.defaultBranch main",
           user=variables.username,
           env_overrides={"HOME": variables.home_dir})
