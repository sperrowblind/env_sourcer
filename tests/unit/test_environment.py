import pytest
from ..conftest import set_env_local
from env_sourcer.models.environment import Environment
from env_sourcer.constants.env_constants import ENVIRONMENTS_MAP


class TestEnvironment():

    def test_local_env(self, set_env_local):
        env = Environment()
        assert env.env in ENVIRONMENTS_MAP['local']