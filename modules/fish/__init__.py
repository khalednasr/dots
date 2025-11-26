import variables
from decman import Module, File, sh

class Fish(Module):
    def __init__(self, enabled):
        super().__init__(name='Fish Shell', enabled=enabled, version=1.0)

    def pacman_packages(self) -> list[str]:
        return ["fish"]
    
    def on_enable(self):
        sh("chsh -s /usr/bin/fish", user=variables.username)

    def files(self) -> dict[str, File]:
        return {
            f"{variables.config_dir}/fish/config.fish": 
                File(source_file=f"./modules/fish/config/config.fish", owner=variables.username)
        }

