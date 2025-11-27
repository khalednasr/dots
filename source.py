import decman
import modules

decman.modules = [
    modules.Core(enabled=True, cpu="amd", gpus=["amd", "nvidia"]),
    modules.Fish(enabled=True),
    modules.Nvim(enabled=True),
    modules.Coding(enabled=True),
    modules.Desktop(enabled=True, laptop=True),
]
