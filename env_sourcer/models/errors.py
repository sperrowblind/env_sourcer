

class InvalidEnvironmentError(Exception):
    def __init__(self, env: str):
        self.message = f'Invalid environment specified: {env}'
        super().__init__(self.message)

class MissingConfigFileError(Exception):
    def __init__(self, env: str):
        self.message = f'Unable to find config file for environment: {env}'
        super().__init__(self.message)

class MissingEnvFolder(Exception):
    def __init__(self):
        self.message = 'Unable to find \'envs\' folder. Please create one and try again'
        super().__init__(self.message)


