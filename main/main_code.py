from functions import main
from pprint import pprint

if __name__ == "__main__":
    def final1_list(final=main()):
        for el in final:
            try:
                print(f"{el['date']} {el['description']}")
                print(f"{el['from']}--->{el['to']}")
                print(f"{el['operationAmount']['amount']}  {el['operationAmount']['currency']['name']}")
                print("")
            except KeyError:
                print(f"{el['date']} {el['description']}")
                print(f"{None}--->{el['to']}")
                print(f"{el['operationAmount']['amount']}  {el['operationAmount']['currency']['name']}")
                print("")


    final1_list()