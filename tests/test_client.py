async def test_async_get_by_id(async_client):
    movie = await async_client.get_by_id(id='tt1000252')
    assert movie.title == 'Blink'


def test_sync_get_by_id(sync_client):
    movie = sync_client.get_by_id(id='tt1000252')
    assert movie.title == 'Blink'


async def test_async_get_by_title(async_client):
    movie = await async_client.get_by_title(title='Rome, open city')
    assert movie.title == 'Rome, Open City'


def test_sync_get_by_title(sync_client):
    movie = sync_client.get_by_title(title='Rome, open city')
    assert movie.title == 'Rome, Open City'


async def test_async_search(async_client):
    items = await async_client.search(text='Spock')
    assert items
    for search_result_item in items:
        assert 'Spock' in search_result_item.title


def test_sync_search(sync_client):
    items = sync_client.search(text='Spock')
    assert items
    for search_result_item in items:
        assert 'Spock' in search_result_item.title


async def test_async_empty_search_result(async_client):
    items = await async_client.search(text='fa34t34gfgra3r3')
    assert items == []


def test_sync_empty_search_result(sync_client):
    items = sync_client.search(text='fa34t34gfgra3r3')
    assert items == []
