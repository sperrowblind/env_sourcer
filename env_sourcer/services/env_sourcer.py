from env_sourcer.models.environment import Environment
import re
from typing import Dict

class EnvSourcer:
    def __init__(self):
        self.env = Environment()
        self.file = self.get_correct_env_file()
        self.env_vars = self.parse_env_file()

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
        print('')
        print('----- Multiple env files located')
        print('----- Please input select index for env file')
        for file in self.env.files:
            print(f'[{self.env.files.index(file)}] {file}')

    # I hate this but didn't feel like figuring out a better way
    def parse_env_file(self) -> Dict:
        with open('envs/'+self.file, 'r') as file:
            env_vars = {
                line.split('=', 1)[0].strip(): self.attempt_to_set_var_type(line.split('=', 1)[1].strip())
                for line in file
                if '=' in line and not line.startswith('[')
            }
        return env_vars

    # This will probably need to be updated in case this converts things that shouldn't be converted
    # Might just keep to bool
    def attempt_to_set_var_type(self, var: str):
        if var in ['True', 'true', 'false', 'False']:
            return bool(var)
        if re.match(r'^-?\d+(?:\.\d+)$', var):
            return float(var)
        if var.isdigit():
            return int(var)
        return var









