from env_sourcer.models.environment import Environment
from env_sourcer.models.errors import InvalidEnvironmentError
from env_sourcer.constants.env_constants import ENVIRONMENTS_MAP
import pytest

class TestEnvironment():

    def test_stg_env_when_valid(self, set_env_stg):
        env = Environment()
        print("Environment set to stg")
        assert env.env in ENVIRONMENTS_MAP['staging']

    def test_local_env_when_valid(self, set_env_local):
        env = Environment()
        print("Environment set to local")
        assert env.env in ENVIRONMENTS_MAP['local']

    def test_prod_env_when_valid(self, set_env_prod):
        env = Environment()
        print("Environment set to prod")
        assert env.env in ENVIRONMENTS_MAP['production']

    def test_invalid_env(self, set_invalid_env):
        with pytest.raises(InvalidEnvironmentError):
            env = Environment()

