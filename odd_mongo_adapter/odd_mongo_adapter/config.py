import os
import logging
from typing import Any


class MissingEnvironmentVariable(Exception):
    pass


def get_env(env: str, default_value: Any = None) -> str:
    try:
        return os.environ[env]
    except KeyError:
        if default_value is not None:
            return default_value
        raise MissingEnvironmentVariable(f'{env} does not exist')


class BaseConfig:
    ODD_HOST = get_env('MONGO_HOST', '@cluster0.qggsn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    ODD_DATABASE = get_env('MONGO_DATABASE', "test_database")
    ODD_USER = get_env('MONGO_USER', 'admin')
    ODD_PASSWORD = get_env('MONGO_PASSWORD', 'admin')

    SCHEDULER_INTERVAL_MINUTES = get_env('SCHEDULER_INTERVAL_MINUTES', 60)


class DevelopmentConfig(BaseConfig):
    FLASK_DEBUG = True
    ENV = 'development'
    DEBUG = True


class ProductionConfig(BaseConfig):
    FLASK_DEBUG = False


def log_env_vars(config: dict):
    logging.info('Environment variables:')
    logging.info(f'MONGO_HOST={config["ODD_HOST"]}')
    logging.info(f'MONGO_DATABASE={config["ODD_DATABASE"]}')
    logging.info(f'MONGO_USER={config["ODD_USER"]}')
    if config["ODD_PASSWORD"] != '':
        logging.info('MONGO_PASSWORD=***')
    logging.info(f'SCHEDULER_INTERVAL_MINUTES={config["SCHEDULER_INTERVAL_MINUTES"]}')
