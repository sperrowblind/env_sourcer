import pytest
from ...env_sourcer.services.env_sourcer import EnvSourcer


class TestEnvSourcer():

    def test_local_env_sourcer_and_attributes(self, set_env_local, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "0")
        sourcer = EnvSourcer()
        assert sourcer.domain == 'google.com_loc'
        assert sourcer.api_key == 'this_is_a_fake_api_key_loc'
        assert sourcer.other_vars.api_key == 'this_is_another_key'


    def test_stg_env_sourcer_and_types(self, set_env_stg, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        sourcer = EnvSourcer()
        assert sourcer.test_password == '12345g6'
        assert isinstance(sourcer.test_password, str)
        assert isinstance(sourcer.test_decimal_1, float)
        print(sourcer.test_decimal_1)
        assert isinstance(sourcer.test_decimal_2, float)
        print(sourcer.test_decimal_2)
        assert isinstance(sourcer.test_decimal_3, float)
        print(sourcer.test_decimal_3)
        assert isinstance(sourcer.do_something, bool)
        assert sourcer.do_something == True

    def test_prod_env_sourcer_and_missing_header(self, set_env_prod):
        sourcer = EnvSourcer()
        assert sourcer.test_key
        with pytest.raises(AttributeError):
            sourcer.dont_work

    def test_stg_env_sourcer_another_file(self, set_env_stg, monkeypatch):
        inputs = iter(['5', '6', '0'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        sourcer = EnvSourcer()
        assert sourcer.api_key == 'another_staging_key_with_another_name'

