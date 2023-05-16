import json
from pprint import pprint
from datetime import datetime


def get_json_list(json_file):
    """Функция возвращает json список"""
    with open(json_file, "r", encoding="utf-8") as file:
        j_list = json.load(file)
        return j_list[-6:]


def get_executed_status(status):
    """Функция возвращает новый список, со всеми выполненными транзакциями"""
    executed_list = []
    for el in status:
        try:
            if el['state'] == 'EXECUTED':
                executed_list.append(el)

        except KeyError:
            continue

    return executed_list


def sorted_data(sorted_d):
    """Функция возвращает список , отсортированный(по убыванию) по дате"""
    sorted_list = sorted(sorted_d, key=lambda x: x['date'], reverse=True)
    return sorted_list


def get_date(dates):
    """Функция возвращает список с датой в формате ^день.месяц.год^"""
    for el in dates:
        get_out_date = datetime.strptime(el['date'], "%Y-%m-%dT%H:%M:%S.%f")
        changed_date = get_out_date.strftime('%d.%m.%Y')
        el['date'] = changed_date
    return dates


def get_card_number(number):
    """Функция возвращает список с  замаскированным номером карты отправителя"""
    for el in number:
        try:
            key_from = el['from']
            card_number_get = key_from.split(" ")
            card_number = card_number_get[-1]
            if len(card_number) == 16:
                hidden_num = f"{''.join(card_number_get[:-1])} {card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"
                el['from'] = hidden_num
            else:
                hidden_num = f"{''.join(card_number_get[:-1])} {card_number[0:4]} {card_number[4:6]}** **** **** {card_number[-4:]}"
                el['from'] = hidden_num
        except KeyError:
            continue
    return number


def get_sent_number(sent_number):
    """Функция возвращает список с  замаскированным номером счёта/ карты получателя"""
    for el in sent_number:
        key_to = el['to']
        num_get = key_to.split(" ")
        sent_card_num = num_get[-1]
        hidden_sent_num = f"{''.join(num_get[:-1])} **{sent_card_num[-4:]}"
        el['to'] = hidden_sent_num
    return sent_number



