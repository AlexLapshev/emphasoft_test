import yaml
from loguru import logger


from api.config.schemas import Settings

with open('api/config/debug-settings.yaml') as f:
    logger.debug('reading settings file')
    settings = yaml.safe_load(f)


def get_api_settings() -> Settings:
    logger.debug('making settings')
    config = {}
    for k, v in settings.items():
        config.update(v)
    origins = config['origins'].split(',')
    config['origins'] = [origin.strip() for origin in origins]
    config = Settings(**config)
    return config


main_config = get_api_settings()
