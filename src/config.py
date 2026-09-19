import yaml
from pathlib import Path


def load(path="configs/config.yaml"):
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(
            f"Config not found at '{config_path.resolve()}'. "
            "Run from the project root, or pass an explicit path."
        )
    return yaml.safe_load(config_path.read_text())
