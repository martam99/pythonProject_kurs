from main.functions import get_json_list, get_executed_status, get_date,sorted_data, get_card_number, get_sent_number


def test_get_json_list():
    expected_result = [
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
            },
            {
                "id": 207126257,
                "state": "EXECUTED",
                "date": "2019-07-15T11:47:40.496961",
                "operationAmount": {
                    "amount": "92688.46",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Открытие вклада",
                "to": "Счет 35737585785074382265"
            },
            {
                "id": 957763565,
                "state": "EXECUTED",
                "date": "2019-01-05T00:52:30.108534",
                "operationAmount": {
                    "amount": "87941.37",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 46363668439560358409",
                "to": "Счет 18889008294666828266"
            },
            {
                "id": 667307132,
                "state": "EXECUTED",
                "date": "2019-07-13T18:51:29.313309",
                "operationAmount": {
                    "amount": "97853.86",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод с карты на счет",
                "from": "Maestro 1308795367077170",
                "to": "Счет 96527012349577388612"
            }
        ]
    assert get_json_list('test_data.json') == expected_result


def test_list():
    status = get_executed_status(get_json_list('test_data.json'))
    expected_result = [
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
            },
            {
                "id": 207126257,
                "state": "EXECUTED",
                "date": "2019-07-15T11:47:40.496961",
                "operationAmount": {
                    "amount": "92688.46",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Открытие вклада",
                "to": "Счет 35737585785074382265"
            },
            {
                "id": 957763565,
                "state": "EXECUTED",
                "date": "2019-01-05T00:52:30.108534",
                "operationAmount": {
                    "amount": "87941.37",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 46363668439560358409",
                "to": "Счет 18889008294666828266"
            },
            {
                "id": 667307132,
                "state": "EXECUTED",
                "date": "2019-07-13T18:51:29.313309",
                "operationAmount": {
                    "amount": "97853.86",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод с карты на счет",
                "from": "Maestro 1308795367077170",
                "to": "Счет 96527012349577388612"
            }
        ]
    assert get_executed_status(status) == expected_result


def test_get_date():
    date = get_date(get_executed_status(get_json_list('test_data.json')))
    expected_result = [
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
            },
            {
                "id": 207126257,
                "state": "EXECUTED",
                "date": "15.07.2019",
                "operationAmount": {
                    "amount": "92688.46",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Открытие вклада",
                "to": "Счет 35737585785074382265"
            },
            {
                "id": 957763565,
                "state": "EXECUTED",
                "date": "05.01.2019",
                "operationAmount": {
                    "amount": "87941.37",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 46363668439560358409",
                "to": "Счет 18889008294666828266"
            },
            {
                "id": 667307132,
                "state": "EXECUTED",
                "date": "13.07.2019",
                "operationAmount": {
                    "amount": "97853.86",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод с карты на счет",
                "from": "Maestro 1308795367077170",
                "to": "Счет 96527012349577388612"
            }
        ]
    assert get_date(date) == expected_result


def test_card_number():
    number = get_card_number(get_date(get_executed_status(get_json_list('test_data.json'))))
    expected_result = [
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
                "from": "Счет 2640 62** **** **** 3262",
                "to": "Счет 20735820461482021315"
            },
            {
                "id": 207126257,
                "state": "EXECUTED",
                "date": "15.07.2019",
                "operationAmount": {
                    "amount": "92688.46",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Открытие вклада",
                "to": "Счет 35737585785074382265"
            },
            {
                "id": 957763565,
                "state": "EXECUTED",
                "date": "05.01.2019",
                "operationAmount": {
                    "amount": "87941.37",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 4636 36** **** **** 8409",
                "to": "Счет 18889008294666828266"
            },
            {
                "id": 667307132,
                "state": "EXECUTED",
                "date": "13.07.2019",
                "operationAmount": {
                    "amount": "97853.86",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод с карты на счет",
                "from": "Maestro 1308 79** **** 7170",
                "to": "Счет 96527012349577388612"
            }

        ]
    assert get_card_number(number) == expected_result


def test_sent_number():
    sent_num = get_sent_number(get_card_number(get_date(get_executed_status(get_json_list('test_data.json')))))
    expected_result = [
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
                "from": "Счет 2640 62** **** **** 3262",
                "to": "Счет **1315"
            },
            {
                "id": 207126257,
                "state": "EXECUTED",
                "date": "15.07.2019",
                "operationAmount": {
                    "amount": "92688.46",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Открытие вклада",
                "to": "Счет **2265"
            },
            {
                "id": 957763565,
                "state": "EXECUTED",
                "date": "05.01.2019",
                "operationAmount": {
                    "amount": "87941.37",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 4636 36** **** **** 8409",
                "to": "Счет **8266"
            },
            {
                "id": 667307132,
                "state": "EXECUTED",
                "date": "13.07.2019",
                "operationAmount": {
                    "amount": "97853.86",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод с карты на счет",
                "from": 'Maestro 1308 79** **** 7170',
                "to": "Счет **8612"
            }
        ]
    assert get_sent_number(sent_num) == expected_result
