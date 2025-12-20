from aura.llm.factory import create_cognitive_engine
from aura.config import load_config, ConfigError
from aura.utils.io import load_text_file, InputError
from aura.pipeline.surface import surface_analysis
from aura.pipeline.semantic import semantic_analysis
from aura.pipeline.inference import inference_analysis


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

    # ENGINE CREATION
    engine = create_cognitive_engine()


    # FREE-FORM ANSWER
    freeform_result = engine.process(
        text=text,
        task="Freeform: raw cognitive engine response (diagnostic)",
        context={
            "experiment": experiment["name"],
            "mode": interpretation["mode"],
        }
    )

    print()
    print("Cognitive engine answer (free-form)")
    print("-" * 27)
    print(freeform_result["text"])

    # WIRE SURFACE AN.
    surface = surface_analysis(text)
    print()
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

    # WIRE SEMANTIC AN.
    semantic = semantic_analysis(
        engine=engine,
        text=text,
        interpretation_mode=interpretation["mode"],
        experiment_name=experiment["name"],
    )
    print()
    print("Semantic analysis")
    print("-" * 16)
    print("Semantic answer (unparsed):")
    print(semantic["explanation"])
    print("Parsed structured data (strict):")
    if semantic["themes"]:
        print("Themes:")
        for t in semantic["themes"]:
            print(f"- {t}")
    else:
        print("Themes: none detected")

    # WIRE INFERENCE AN.
    inference = inference_analysis(
        engine=engine,
        text=text,
        interpretation_mode=interpretation["mode"],
        experiment_name=experiment["name"],
    )

    print()
    print("Inference analysis")
    print("-" * 18)
    print("Inference answer (unparsed):")
    print(inference["explanation"])

    print("Parsed structured data (strict):")
    if inference["entities"]:
        print("Entities:")
        for e in inference["entities"]:
            print(f"- {e}")
    else:
        print("Entities: none detected")

    if inference["events"]:
        print("Events:")
        for ev in inference["events"]:
            print(f"- {ev}")
    else:
        print("Events: none detected")
