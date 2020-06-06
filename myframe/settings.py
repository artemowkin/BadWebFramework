import os
import importlib

DEFAULT_ENV_NAME = 'MYFRAME_SETTINGS_MODULE'


class Settings:

    def __init__(self):
        env_settings = self._get_env_settings_module()
        self.settings_module = importlib.import_module(env_settings)

    def _get_env_settings_module(self):
        env = os.environ.get(DEFAULT_ENV_NAME)
        if not env:
            raise ValueError(f'You need to set up {DEFAULT_ENV_NAME}')

        return env

    def __getattr__(self, item):
        if not hasattr(self.settings_module, item):
            raise ValueError(f'Settings module does not have attr {item}')

        return getattr(self.settings_module, item)


settings = Settings()
