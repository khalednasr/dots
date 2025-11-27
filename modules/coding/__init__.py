from decman import Module, File, sh
import variables

class Coding(Module):
    def __init__(self, enabled, languages=["python", "rust", "cpp"], toolkits=[]):
        super().__init__(name='Core', enabled=enabled, version=1.03)
        self.languages = languages
        self.toolkits = toolkits

    def pacman_packages(self) -> list[str]:
        # Utilities
        packages = ["direnv"]

        if "python" in self.languages:
            packages += ["pixi", "uv"]

        if "rust" in self.languages:
            packages += ["rustup"]

        if "cpp" in self.languages:
            packages += ["cmake"]

        return packages

    def on_enable(self):
        if "rust" in self.languages:
            sh(f"HOME={variables.home_dir} rustup default stable", user=variables.username)

    def files(self) -> dict[str, File]:
        return {
            f"{variables.config_dir}/direnv/direnv.toml":
                File(content='[global]\nlog_filter="^$"', owner=variables.username)
        }
