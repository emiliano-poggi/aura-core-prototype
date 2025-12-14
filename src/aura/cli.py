import click
from aura.runner import run_experiment

@click.group()
def main():
    """A.U.R.A. Core Prototype CLI"""
    pass

@main.command()
@click.argument("config_path", type=click.Path(exists=True))
def run(config_path):
    """Run an AURA experiment from a YAML configuration."""
    click.echo(f"Running experiment: {config_path}")
    run_experiment(config_path)

if __name__ == "__main__":
    main()
