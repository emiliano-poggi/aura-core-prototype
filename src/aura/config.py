from pathlib import Path
import yaml

class ConfigError(Exception):
    pass

def load_config(path: str) -> dict:
    config_path = Path(path)

    if not config_path.exists():
        raise ConfigError(f"Config file does not exist: {path}")

    with config_path.open("r", encoding="utf-8") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ConfigError(f"Invalid YAML syntax: {e}")

    if not isinstance(data, dict):
        raise ConfigError("Config root must be a YAML mapping")

    _validate_config(data)

    return data


def _validate_config(cfg: dict) -> None:
    # ---- experiment ----
    experiment = cfg.get("experiment")
    if not isinstance(experiment, dict):
        raise ConfigError("Missing or invalid 'experiment' section")

    name = experiment.get("name")
    if not isinstance(name, str) or not name.strip():
        raise ConfigError("experiment.name must be a non-empty string")

    # ---- input ----
    input_cfg = cfg.get("input")
    if not isinstance(input_cfg, dict):
        raise ConfigError("Missing or invalid 'input' section")

    source = input_cfg.get("source")
    if source != "file":
        raise ConfigError("input.source must be 'file'")

    path = input_cfg.get("path")
    if not isinstance(path, str):
        raise ConfigError("input.path must be a string")

    input_path = Path(path)
    if not input_path.exists():
        raise ConfigError(f"Input file does not exist: {path}")

    # ---- interpretation ----
    interpretation = cfg.get("interpretation")
    if not isinstance(interpretation, dict):
        raise ConfigError("Missing or invalid 'interpretation' section")

    mode = interpretation.get("mode")
    if mode not in ("structured", "unstructured"):
        raise ConfigError(
            "interpretation.mode must be either 'structured' or 'unstructured'"
        )
