from src.processing import filter_by_state, sort_by_date


def test_filter_by_state():
    operations = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    # Проверка фильтрации по умолчанию
    result = filter_by_state(operations)
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)

    # Проверка фильтрации по CANCELED
    result = filter_by_state(operations, "CANCELED")
    assert len(result) == 2
    assert all(op["state"] == "CANCELED" for op in result)


def test_sort_by_date():
    operations = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    # Проверка сортировки по убыванию
    result = sort_by_date(operations)
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert result == expected

    # Проверка сортировки по возрастанию
    result = sort_by_date(operations, descending=False)
    expected = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
    assert result == expected


def test_filter_by_state(sample_operations):
    filtered = filter_by_state(sample_operations, "EXECUTED")
    assert len(filtered) > 0
    # Другие тесты


def test_sort_by_date(sample_operations):
    sorted_ops = sort_by_date(sample_operations)
    # Проверяем сортировку
