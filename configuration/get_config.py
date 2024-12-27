import yaml
from configuration.env import get_environment

env = get_environment()

def get_config(env=env):
    with open('users/directory/pycharmProjects/PythonProjectAPI1/configuration/config.yaml', 'r') as f:
        config_data = yaml.load(f, Loader=yaml.FullLoader)
        config = config_data[env]
        return config

### set absolute path /pycharmProjects/PythonProjectAPI1/configuration/config.yaml