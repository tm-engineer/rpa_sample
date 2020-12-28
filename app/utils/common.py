import environ


def load_env(file_name='.env'):
    env = environ.Env(DEBUG=(bool, False))
    BASE_DIR = environ.Path(__file__) - 2
    env.read_env(BASE_DIR(file_name))
    return env
