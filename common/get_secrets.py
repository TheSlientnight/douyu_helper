import os


def get_secrets(item):
    return os.environ[item]
