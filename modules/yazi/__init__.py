from decman import Module, Directory, sh
import variables

class Yazi(Module):
    def __init__(self, enabled):
        super().__init__(name='Yazi', enabled=enabled, version=1.0)

    def pacman_packages(self) -> list[str]:
        return [
            "yazi",
            "fd",
            "ffmpeg",
            "7zip",
            "jq",
            "poppler",
            "ripgrep",
            "fzf",
            "zoxide",
            "resvg",
            "imagemagick",
            "trash-cli",
        ]

    def directories(self) -> dict[str, Directory]:
        # self.add_plugins()
        return {
            f"{variables.config_dir}/yazi":
                Directory(source_directory="./modules/yazi/config", owner=variables.username)
        }

    def add_plugins(self):
        sh(f"rm -rf {variables.config_dir}/yazi/plugins")
        sh(f"rm {variables.config_dir}/yazi/package.toml")
        sh("ya pkg add uhs-robert/recycle-bin", user=variables.username, env_overrides={"HOME": variables.home_dir})
        sh("ya pkg add pirafrank/what-size", user=variables.username, env_overrides={"HOME": variables.home_dir})

    def on_enable(self):
        self.add_plugins()
