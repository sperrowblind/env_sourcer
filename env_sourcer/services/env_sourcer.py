from env_sourcer.models.environment import Environment
from env_sourcer.models.section import Section
import re
from typing import Dict

class EnvSourcer:
    def __init__(self):
        self.env = Environment()
        self.file = self.get_correct_env_file()
        self.env_vars = self.parse_env_file()
        self._create_attributes()

    def _create_attributes(self):
        for key, value in self.env_vars.items():
            if isinstance(value, dict):
                setattr(self, key.lower(), Section(value))
            else:
                setattr(self, key.lower(), value)

    def __getattr__(self, name):
        if name in self.env_vars:
            return self.env_vars[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def get_correct_env_file(self) -> str:
        if len(self.env.files) > 1:
            self.print_multiple_files()
            env_index = int(input('----- Input selection here: '))
            while env_index > len(self.env.files) or env_index < 0:
                print('----- Invalid input')
                self.print_multiple_files()
                env_index = int(input('----- Input selection here: '))
        else:
            env_index = 0
        return self.env.files[env_index]

    def print_multiple_files(self):
        print('\n----- Multiple env files located')
        print('----- Please input select index for env file')
        for file in self.env.files:
            print(f'[{self.env.files.index(file)}] {file}')

    # I hate this but didn't feel like figuring out a better way
    def parse_env_file(self) -> Dict:
        env_vars = {}
        last_header = None
        with open('envs/'+self.file, 'r') as file:
            for line in file:
                if line.startswith('[') and line.endswith(']\n'):
                    last_header = str.lower(line[1:-2].replace(' ', '_'))
                    env_vars[last_header] = {}
                    continue
                key = str.lower(line.split('=', 1)[0].strip())
                if '=' in line and not line.startswith('['):
                    var = line.split('=', 1)[1].strip()
                    env_vars.setdefault(key, self.attempt_to_set_var_type(var))
                    if last_header:
                        env_vars[last_header][key] = self.attempt_to_set_var_type(var)

        return env_vars

    # This will probably need to be updated in case this converts things that shouldn't be converted
    # Might just keep to bool
    def attempt_to_set_var_type(self, var: str):
        if var in ['True', 'true', 'TRUE']:
            return True
        if var in ['False', 'false', 'FALSE']:
            return False
        if re.match(r'^-?\d+(?:\.\d+)$', var):
            return float(var)
        if var.isdigit():
            return int(var)
        return var

