import csv

def get_cvs_data():
    exit_list = []

    with open('pricetilda.csv', 'r', encoding='utf-8') as f:
        data = csv.DictReader(f, delimiter=';')
        for row in data:
            exit_list.append(row)
        print(exit_list)
        return exit_list