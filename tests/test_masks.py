import pytest

from src.masks import get_mask_account, get_mask_card_number


# Используем параметризацию для карт
@pytest.mark.parametrize(
    "card_number,expected",
    [
        ("4500123456789012", "4500 12** **** 9012"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("7000792289606361", "7000 79** **** 6361"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Используем параметризацию для счетов
@pytest.mark.parametrize(
    "account_number,expected",
    [
        ("40817810000000000000", "** 0000"),
        ("12345678901234567890", "** 7890"),
        ("abcd1234abcd1234", "** 1234"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


# Добавляем тесты с использованием фикстур
def test_mask_card_with_fixture(card_numbers):
    for number in card_numbers:
        # Здесь можно добавить логику проверки
        get_mask_card_number(number)


def test_mask_account_with_fixture(account_numbers):
    for number in account_numbers:
        # Здесь можно добавить логику проверки
        get_mask_account(number)
