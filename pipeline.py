import importlib
import yaml

# Shared state — imported by every stage, never recreated
data = {}

def run():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)

    for stage_name in config["stages"]:
        stage = importlib.import_module(stage_name)
        stage.run(data, config)

if __name__ == "__main__":
    run()
