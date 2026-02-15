from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(sample_operations):
    filtered = filter_by_state(sample_operations, 'EXECUTED')
    assert len(filtered) > 0
    # Другие тесты

def test_sort_by_date(sample_operations):
    sorted_ops = sort_by_date(sample_operations)
    # Проверяем сортировку