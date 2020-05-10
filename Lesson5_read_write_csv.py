import csv


def write_csv(data):
    with open('names.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'], data['surname'], data['age']))


def write_csv2(data):
    with open('names.csv', 'a') as file:
        order = ['name', 'surname', 'age']
        writer = csv.DictWriter(file, fieldnames=order)

        writer.writerow(data)


def read_csv():
	with open('cmc.csv') as file:
    	order = ['name', 'url', 'price']
    	reader = csv.DictReader(file, fieldnames=order)
    return reader
