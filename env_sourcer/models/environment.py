from env_sourcer.constants.env_constants import (ENVIRONMENTS, ENVIRONMENTS_MAP)
from env_sourcer.models.errors import (
    MissingConfigFileError,
    MissingEnvFolder,
    InvalidEnvironmentError
)
from os import (getenv, listdir)
from os.path import exists

class Environment():

    def __init__(self):
        self.files = []
        self.env = self.get_env()

    def _verify_valid_environment(self, environment: str):
        return environment in ENVIRONMENTS

    def _verify_env_folder(self):
        return exists('envs/')

    def _verify_env_file_exists(self, environment: str):
        self.files = []
        for file in listdir('envs'):
            try:
                if self._is_valid_file(file, environment):
                    self.files.append(file)
            except:
                continue
        if len(self.files) != 0:
            return True
        return False

    def _is_valid_file(self, file: str, environment: str):
        return str.split(file, '.')[1] in ENVIRONMENTS_MAP[environment]

    def get_env(self):
        if not self._verify_env_folder():
            raise MissingEnvFolder
        environment = str.lower(getenv('ENVIRONMENT'))
        if not self._verify_valid_environment(environment):
            raise InvalidEnvironmentError(environment)
        if not self._verify_env_file_exists(environment):
            raise MissingConfigFileError(environment)

        return environment

