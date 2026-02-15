import pytest


@pytest.fixture
def sample_operations():
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "description": "Перевод с карты на карту",
            "operation_id": 56789,
            "amount": {"amount": 10000, "currency": "RUB"},
        },
        # Другие тестовые операции
    ]
