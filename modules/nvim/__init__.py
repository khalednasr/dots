from decman import Module, sh

class Nvim(Module):
    def __init__(self, enabled):
        super().__init__(name='Neovim', enabled=enabled, version=1.0)
    
    def pacman_packages(self) -> list[str]:
        return [
            "neovim",
            "fzf",
            "ripgrep",
        ]
