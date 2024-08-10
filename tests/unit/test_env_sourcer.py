import pytest
from ..conftest import set_env_local
from env_sourcer.services.env_sourcer import EnvSourcer
from env_sourcer.constants.env_constants import ENVIRONMENTS_MAP


class TestEnvSourcer():

    def test_local_env_sourcer(self, set_env_local):
        sourcer = EnvSourcer()
        print(sourcer.file)
        print(sourcer.env_vars)
        #assert env.env in ENVIRONMENTS_MAP['local']