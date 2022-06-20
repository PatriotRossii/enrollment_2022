import pytest

from analyzer.utils.testing import compare_nodes, import_batches

ROOT_ID = "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1"
IMPORT_BATCHES = [
    {
        "items": [
            {
                "type": "CATEGORY",
                "name": "Товары",
                "id": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
                "parentId": None,
            }
        ],
        "updateDate": "2022-02-01T12:00:00Z",
    },
    {
        "items": [
            {
                "type": "CATEGORY",
                "name": "Смартфоны",
                "id": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
            },
            {
                "type": "OFFER",
                "name": "jPhone 13",
                "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                "price": 79999,
            },
            {
                "type": "OFFER",
                "name": "Xomiа Readme 10",
                "id": "b1d8fd7d-2ae3-47d5-b2f9-0f094af800d4",
                "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                "price": 59999,
            },
        ],
        "updateDate": "2022-02-02T12:00:00Z",
    },
    {
        "items": [
            {
                "type": "CATEGORY",
                "name": "Телевизоры",
                "id": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
            },
            {
                "type": "OFFER",
                "name": 'Samson 70" LED UHD Smart',
                "id": "98883e8f-0507-482f-bce2-2fb306cf6483",
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "price": 32999,
            },
            {
                "type": "OFFER",
                "name": 'Phyllis 50" LED UHD Smarter',
                "id": "74b81fda-9cdc-4b63-8927-c978afed5cf4",
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "price": 49999,
            },
        ],
        "updateDate": "2022-02-03T12:00:00Z",
    },
    {
        "items": [
            {
                "type": "OFFER",
                "name": 'Goldstar 65" LED UHD LOL Very Smart',
                "id": "73bc3b36-02d1-4245-ab35-3106c9ee1c65",
                "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                "price": 69999,
            }
        ],
        "updateDate": "2022-02-03T15:00:00Z",
    },
]

EXPECTED_TREE = {
    "type": "CATEGORY",
    "name": "Товары",
    "id": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
    "price": 58599,
    "parentId": None,
    "date": "2022-02-03T15:00:00Z",
    "children": [
        {
            "type": "CATEGORY",
            "name": "Телевизоры",
            "id": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
            "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
            "price": 50999,
            "date": "2022-02-03T15:00:00Z",
            "children": [
                {
                    "type": "OFFER",
                    "name": 'Samson 70" LED UHD Smart',
                    "id": "98883e8f-0507-482f-bce2-2fb306cf6483",
                    "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                    "price": 32999,
                    "date": "2022-02-03T12:00:00Z",
                    "children": None,
                },
                {
                    "type": "OFFER",
                    "name": 'Phyllis 50" LED UHD Smarter',
                    "id": "74b81fda-9cdc-4b63-8927-c978afed5cf4",
                    "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                    "price": 49999,
                    "date": "2022-02-03T12:00:00Z",
                    "children": None,
                },
                {
                    "type": "OFFER",
                    "name": 'Goldstar 65" LED UHD LOL Very Smart',
                    "id": "73bc3b36-02d1-4245-ab35-3106c9ee1c65",
                    "parentId": "1cc0129a-2bfe-474c-9ee6-d435bf5fc8f2",
                    "price": 69999,
                    "date": "2022-02-03T15:00:00Z",
                    "children": None,
                },
            ],
        },
        {
            "type": "CATEGORY",
            "name": "Смартфоны",
            "id": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
            "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
            "price": 69999,
            "date": "2022-02-02T12:00:00Z",
            "children": [
                {
                    "type": "OFFER",
                    "name": "jPhone 13",
                    "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                    "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                    "price": 79999,
                    "date": "2022-02-02T12:00:00Z",
                    "children": None,
                },
                {
                    "type": "OFFER",
                    "name": "Xomiа Readme 10",
                    "id": "b1d8fd7d-2ae3-47d5-b2f9-0f094af800d4",
                    "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                    "price": 59999,
                    "date": "2022-02-02T12:00:00Z",
                    "children": None,
                },
            ],
        },
    ],
}


@pytest.mark.asyncio
async def test_import(client):
    await import_batches(client, IMPORT_BATCHES, 200)

    response = await client.get(f"/nodes/{ROOT_ID}")
    assert response.status_code == 200
    compare_nodes(response.json(), EXPECTED_TREE)


@pytest.mark.asyncio
async def test_import_update(client):
    expected_tree = {
        "type": "CATEGORY",
        "name": "Товары",
        "id": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
        "price": 37499,
        "parentId": None,
        "date": "2022-02-02T13:00:00Z",
        "children": [
            {
                "type": "CATEGORY",
                "name": "Смартфоны",
                "id": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
                "price": 37499,
                "date": "2022-02-02T13:00:00Z",
                "children": [
                    {
                        "type": "OFFER",
                        "name": "Samsung 2022",
                        "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                        "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                        "price": 15000,
                        "date": "2022-02-02T13:00:00Z",
                        "children": None,
                    },
                    {
                        "type": "OFFER",
                        "name": "Xomiа Readme 10",
                        "id": "b1d8fd7d-2ae3-47d5-b2f9-0f094af800d4",
                        "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                        "price": 59999,
                        "date": "2022-02-02T12:00:00Z",
                        "children": None,
                    },
                ],
            },
        ],
    }

    await import_batches(client, IMPORT_BATCHES[:2], 200)
    await import_batches(
        client,
        [
            {
                "items": [
                    {
                        "type": "OFFER",
                        "name": "Samsung 2022",
                        "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                        "parentId": "d515e43f-f3f6-4471-bb77-6b455017a2d2",
                        "price": 15000,
                    }
                ],
                "updateDate": "2022-02-02T13:00:00Z",
            }
        ],
        200,
    )

    response = await client.get(f"/nodes/{ROOT_ID}")
    assert response.status_code == 200
    compare_nodes(response.json(), expected_tree)


@pytest.mark.asyncio
async def test_import_type_change(client):
    batches = [
        {
            "items": [
                {
                    "type": "CATEGORY",
                    "name": "Товары",
                    "id": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
                    "parentId": None,
                },
                {
                    "type": "OFFER",
                    "name": "Item",
                    "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                    "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
                    "price": 1000,
                },
            ],
            "updateDate": "2022-02-01T12:00:00Z",
        },
    ]
    expected_tree = {
        "type": "CATEGORY",
        "name": "Товары",
        "id": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
        "price": 1000,
        "parentId": None,
        "date": "2022-02-01T12:00:00Z",
        "children": [
            {
                "type": "OFFER",
                "name": "Item",
                "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                "price": 1000,
                "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
                "date": "2022-02-01T12:00:00Z",
                "children": None,
            }
        ],
    }

    await import_batches(client, batches, 200)
    await import_batches(
        client,
        [
            {
                "items": [
                    {
                        "type": "OFFER",
                        "name": "Товары",
                        "id": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
                        "parentId": None,
                    }
                ],
                "updateDate": "2022-02-01T12:00:00Z",
            }
        ],
        400,
    )
    await import_batches(
        client,
        [
            {
                "items": [
                    {
                        "type": "CATEGORY",
                        "name": "Item",
                        "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                        "parentId": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
                        "price": None,
                    }
                ],
                "updateDate": "2022-02-01T12:00:00Z",
            }
        ],
        400,
    )

    # Проверка, что структура осталась прежней

    response = await client.get(f"/nodes/{ROOT_ID}")
    assert response.status_code == 200
    compare_nodes(response.json(), expected_tree)


@pytest.mark.asyncio
async def test_import_category_price(client):
    batches = [
        {
            "items": [
                {
                    "type": "CATEGORY",
                    "name": "Товары",
                    "id": "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1",
                    "parentId": None,
                    "price": 1000,
                }
            ],
            "updateDate": "2022-02-01T12:00:00Z",
        }
    ]
    await import_batches(client, batches, 400)


@pytest.mark.asyncio
async def test_import_empty(client):
    await import_batches(client, [{"items": [], "updateDate": "2022-02-01T12:00:00Z"}], 200)


@pytest.mark.asyncio
async def test_import_change_parent(client):
    goods_root_id = "069cb8d7-bbdd-47d3-ad8f-82ef4c269df1"
    people_root_id = "069cb8d7-bbdd-47d3-ad8f-82ef4c269df2"

    batches = [
        {
            "items": [
                {
                    "type": "CATEGORY",
                    "name": "Товары",
                    "id": goods_root_id,
                    "parentId": None,
                },
                {
                    "type": "OFFER",
                    "name": "Товар",
                    "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                    "parentId": goods_root_id,
                    "price": 1000,
                },
                {
                    "type": "CATEGORY",
                    "name": "Люди",
                    "id": people_root_id,
                    "parentId": None,
                },
            ],
            "updateDate": "2022-02-01T12:00:00Z",
        },
        {
            "items": [
                {
                    "type": "OFFER",
                    "name": "Человек",
                    "id": "863e1a7a-1304-42ae-943b-179184c077e4",
                    "parentId": people_root_id,
                    "price": 49000,
                }
            ],
            "updateDate": "2022-02-01T15:00:00Z",
        },
        {
            "items": [
                {
                    "type": "OFFER",
                    "name": "Человек",
                    "id": "863e1a7a-1304-42ae-943b-179184c077e4",
                    "parentId": goods_root_id,
                    "price": 49000,
                }
            ],
            "updateDate": "2022-02-01T16:00:00Z",
        },
    ]

    expected_goods_tree = {
        "type": "CATEGORY",
        "name": "Товары",
        "id": goods_root_id,
        "price": 25000,
        "parentId": None,
        "date": "2022-02-01T16:00:00Z",
        "children": [
            {
                "type": "OFFER",
                "name": "Товар",
                "id": "863e1a7a-1304-42ae-943b-179184c077e3",
                "price": 1000,
                "parentId": goods_root_id,
                "date": "2022-02-01T12:00:00Z",
                "children": None,
            },
            {
                "type": "OFFER",
                "name": "Человек",
                "id": "863e1a7a-1304-42ae-943b-179184c077e4",
                "price": 49000,
                "parentId": goods_root_id,
                "date": "2022-02-01T16:00:00Z",
                "children": None,
            },
        ],
    }

    expected_people_tree = {
        "type": "CATEGORY",
        "name": "Люди",
        "id": people_root_id,
        "price": None,
        "parentId": None,
        "date": "2022-02-01T16:00:00Z",
        "children": [],
    }

    await import_batches(client, batches, 200)

    response = await client.get(f"/nodes/{goods_root_id}")
    assert response.status_code == 200
    compare_nodes(response.json(), expected_goods_tree)

    response = await client.get(f"/nodes/{people_root_id}")
    assert response.status_code == 200
    compare_nodes(response.json(), expected_people_tree)
