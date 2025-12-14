from aura.config import load_config, ConfigError
from aura.utils.io import load_text_file, InputError
from aura.pipeline.surface import surface_analysis

def run_experiment(config_path: str) -> None:
    try:
        cfg = load_config(config_path)
    except ConfigError as e:
        print(f"[ERROR] {e}")
        return

    experiment = cfg["experiment"]
    input_cfg = cfg["input"]
    interpretation = cfg["interpretation"]

    try:
        text = load_text_file(input_cfg["path"])
    except InputError as e:
        print(f"[ERROR] {e}")
        return
        
    print()
    print("Experiment loaded successfully")
    print("-" * 29)
    print(f"Name: {experiment['name']}")

    description = experiment.get("description")
    if description:
        print(f"Description: {description.strip()}")

    print(f"Input source: {input_cfg['source']}")
    print(f"Input path: {input_cfg['path']}")
    print(f"Interpretation mode: {interpretation['mode']}")
    print(f"Input text length: {len(text)} characters")
    print()

    surface = surface_analysis(text)
    print("Surface analysis")
    print("-" * 16)
    print(f"Characters: {surface['length']['characters']}")
    print(f"Words: {surface['length']['words']}")
    print(f"Lines: {surface['length']['lines']}")
    print(f"Sentences: {surface['fragmentation']['sentences']}")
    print(
        f"Avg words/sentence: "
        f"{surface['fragmentation']['avg_words_per_sentence']}"
    )
    print(f"Ellipses: {surface['fragmentation']['ellipsis_count']}")
    print(
        f"Newline density: "
        f"{surface['fragmentation']['newline_density']}"
    )