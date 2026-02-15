import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    # Базовые случаи
    assert get_mask_card_number("4500123456789012") == "4500 12** **** 9012"
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"

    # Проверка исключения для короткого номера
    with pytest.raises(ValueError):
        get_mask_card_number("12345678")


def test_get_mask_account():
    # Базовые случаи
    assert get_mask_account("40817810000000000000") == "** 0000"

    # Короткие номера
    assert get_mask_account("123456") == "** 3456"  # Исправленный ожидаемый результат

    # Длинные номера
    assert get_mask_account("12345678901234567890") == "** 7890"

    # Нечисловые символы
    assert get_mask_account("abcd1234abcd1234") == "** 1234"


def test_invalid_data():
    # Невалидные входные данные
    with pytest.raises(TypeError):
        get_mask_card_number(None)

    with pytest.raises(TypeError):
        get_mask_account(None)

    assert get_mask_card_number('') == ''
    assert get_mask_account('') == ''
