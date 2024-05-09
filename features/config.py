import yaml

def get_config(config_file):
    with open(config_file) as input:
        return yaml.safe_load(input)
