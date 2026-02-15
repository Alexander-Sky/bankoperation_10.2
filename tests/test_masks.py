from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("4500123456789012") == "4500 12** **** 9012"
    # Другие тесты


def test_get_mask_account():
    assert get_mask_account("40817810000000000000") == "** 0000"
    # Другие тесты
