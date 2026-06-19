import yaml

def run(data, config):
    budget_file = config["parameters"] + ".yaml"
    with open(budget_file) as f:
        budget = yaml.safe_load(f)
    data.update(budget)
