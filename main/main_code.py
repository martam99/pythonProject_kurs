from functions import get_json_list, get_executed_status, sorted_data, get_date, get_card_number, get_sent_number
from pprint import pprint

if __name__ == "__main__":
    def final1_list():
        file_name = get_json_list('file.json')
        executed = get_executed_status(file_name)
        sorted_l = sorted_data(executed)
        date = get_date(sorted_l)
        card_num = get_card_number(date)
        sent_num = get_sent_number(card_num)
        for el in sent_num:
            if 'from' in el:
                print(f"{el['date']} {el['description']}")
                print(f"{el['from']}--->{el['to']}")
                print(f"{el['operationAmount']['amount']}  {el['operationAmount']['currency']['name']}")
                print("")
            else:
                print(f"{el['date']} {el['description']}")
                print(f"{None}--->{el['to']}")
                print(f"{el['operationAmount']['amount']}  {el['operationAmount']['currency']['name']}")
                print("")


    final1_list()