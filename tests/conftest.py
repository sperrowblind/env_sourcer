import pytest
import os
from unittest import mock


@pytest.fixture()
def set_env_local(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "local")
    yield

@pytest.fixture()
def set_env_stg(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "stg")
    yield

@pytest.fixture()
def set_env_prod(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "prod")
    yield

@pytest.fixture()
def set_invalid_env(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "random")
    yield


