import decman
import modules

decman.modules = [
    modules.Core(enabled=True),
    modules.Fish(enabled=True),
    modules.Nvim(enabled=True),
    modules.Desktop(enabled=True, laptop=True),
]
