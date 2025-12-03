from decman import Module, File, sh
import variables

class Core(Module):
    def __init__(self, enabled):
        super().__init__(name='Core', enabled=enabled, version=1.0)

    def pacman_packages(self) -> list[str]:
        packages = [
            f"{variables.cpu}-ucode",
            "base",
            "base-devel",
            "efibootmgr",
            "linux",
            "linux-firmware",
            "networkmanager",
            "zram-generator",
            "grub",
            "reflector",

            # CLI tools
            "less",
            "git",
            "github-cli",
            "ouch",
        ]

        if "nvidia" in variables.gpus:
            packages += ["nvidia-open", "nvidia-settings"]

        if variables.dualboot:
            packages += [
                "ntfs-3g",  # for mounting windows NTFS drives
                "os-prober",  # for grub to find windows
                "fuse3",  # also for grub to find windows
            ]

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

        if variables.dualboot:
            sh("echo GRUB_DISABLE_OS_PROBER=false >> /etc/default/grub")
            sh("grub-mkconfig -o /boot/grub/grub.cfg")

    def files(self) -> dict[str, File]:
        return {
            # Pacman config
            # Niri config
            "/etc/pacman.conf":
                File(source_file="./modules/core/config/pacman/pacman.conf"),
        }
