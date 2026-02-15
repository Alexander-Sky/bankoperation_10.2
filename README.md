# Банковский виджет операций

## Описание проекта
Проект представляет собой набор инструментов для обработки банковских операций. 
Основные функции включают фильтрацию и сортировку операций по различным критериям.

## Установка

### Требования
* Python 3.14+
* Poetry для управления зависимостями

### Установка проекта
```bash
# Клонирование репозитория
git clone <git@github.com:Alexander-Sky/bankoperation_10.2.git>

##Установка зависимостей
Необходимо установить

poetry install
poetry shell

Или с помощью pip:

pip install -r requirements.txt

## Использование

###Импорт функций

```python
from src.processing import filter_by_state, sort_by_date

##Примеры работы

###Пример фильтрации операций

operations = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

####Фильтрация по умолчанию (EXECUTED)

filtered_operations = filter_by_state(operations)

###Фильтрация по CANCELED

cancelled_operations = filter_by_state(operations, 'CANCELED')

2. **В модуле processing.py** сами функции уже должны быть реализованы:
```python
from typing import List, Dict

def filter_by_state(operations: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Фильтрация операций по состоянию"""
    return [op for op in operations if op.get('state') == state]

def sort_by_date(operations: List[Dict], descending: bool = True) -> List[Dict]:
    """Сортировка операций по дате"""
    return sorted(operations, key=lambda x: x['date'], reverse=descending)

3. В тестах (tests/test_processing.py) должны быть проверки работы функций:

python

def test_filter_by_state():
    # Тестовые данные и проверки
    ...

def test_sort_by_date():
    # Тестовые данные и проверки
    ...

