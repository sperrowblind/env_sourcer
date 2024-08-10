import pytest
import os
from unittest import mock


@pytest.fixture()
def set_env_local(monkeypatch):
    with mock.patch.dict(os.environ, clear=True):
        monkeypatch.setenv("ENVIRONMENT", "local")
        yield

@pytest.fixture()
def set_env_stg(monkeypatch):
    with mock.patch.dict(os.environ, clear=True):
        monkeypatch.setenv("ENVIRONMENT", "stg")
        yield

@pytest.fixture()
def set_env_prod(monkeypatch):
    with mock.patch.dict(os.environ, clear=True):
        monkeypatch.setenv("ENVIRONMENT", "prod")
        yield


