from main.functions import get_executed_status, sorted_data, get_card_number, get_date, get_sent_number
import pytest


@pytest.fixture
def transactions():
    return [{
        "id": 27192367,
        "state": "CANCELED",
        "date": "2018-12-24T20:16:18.819037",
        "operationAmount": {
            "amount": "991.49",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 71687416928274675290",
        "to": "Счет 87448526688763159781"
    },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315"
        }]


def test_get_executed_status(transactions):
    assert get_executed_status(transactions) == [
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315"
        }]


def test_sorted_data(transactions):
    assert sorted_data(transactions) == [
        {
            "id": 27192367,
            "state": "CANCELED",
            "date": "2018-12-24T20:16:18.819037",
            "operationAmount": {
                "amount": "991.49",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 71687416928274675290",
            "to": "Счет 87448526688763159781"
        },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315"
        }
    ]


def test_get_date(transactions):
    assert get_date(transactions) == [{
        "id": 27192367,
        "state": "CANCELED",
        "date": "24.12.2018",
        "operationAmount": {
            "amount": "991.49",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 71687416928274675290",
        "to": "Счет 87448526688763159781"
    },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "09.03.2018",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет 20735820461482021315"
        }]


def test_card_number(transactions):
    assert get_card_number(transactions) == [
      {
          "id": 27192367,
          "state": "CANCELED",
          "date": "2018-12-24T20:16:18.819037",
          "operationAmount": {
              "amount": "991.49",
              "currency": {
                  "name": "руб.",
                  "code": "RUB"
              }
          },
          "description": "Перевод со счета на счет",
          "from": "Счет 7168 74** **** **** 5290",
          "to": "Счет 87448526688763159781"
      },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 2640 62** **** **** 3262",
            "to": "Счет 20735820461482021315"
        }]


def test_sent_number(transactions):
    assert get_sent_number(transactions) == [{
        "id": 27192367,
        "state": "CANCELED",
        "date": "2018-12-24T20:16:18.819037",
        "operationAmount": {
            "amount": "991.49",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 71687416928274675290",
        "to": "Счет **9781"
    },
        {
            "id": 921286598,
            "state": "EXECUTED",
            "date": "2018-03-09T23:57:37.537412",
            "operationAmount": {
                "amount": "25780.71",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 26406253703545413262",
            "to": "Счет **1315"
        }]
