import os

import pytest

from aio_omdb.client import AsyncOMDBClient, SyncOMDBClient


@pytest.fixture(scope='session')
def api_key() -> str:
    return os.environ['OMDB_API_KEY']


@pytest.fixture(scope='session')
def async_client(api_key: str) -> AsyncOMDBClient:
    return AsyncOMDBClient(api_key=api_key)


@pytest.fixture(scope='session')
def sync_client(api_key: str) -> SyncOMDBClient:
    return SyncOMDBClient(api_key=api_key)
