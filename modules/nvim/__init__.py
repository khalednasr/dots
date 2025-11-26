from decman import Module, Directory, sh
import variables

class Nvim(Module):
    def __init__(self, enabled):
        super().__init__(name='Neovim', enabled=enabled, version=1.0)
    
    def pacman_packages(self) -> list[str]:
        return [
            "neovim",
            "fzf",
            "ripgrep",
        ]

    def directories(self) -> dict[str, Directory]:
        return {
            f"{variables.config_dir}/nvim": 
                Directory(source_directory=f"./modules/nvim/config", owner=variables.username)
        }
