import yaml

def get_config(path):
    with open(path) as input:
        return yaml.safe_load(input)
