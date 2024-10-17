import csv

class NewDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = ';'
    delimiter = '!'
    lineterminator = '\n'

csv.register_dialect('task3', NewDialect)


with open('industry_sic.csv', 'w') as f:
    writer = csv.writer(f, dialect='task3')
    writer.writerow(['100000', 'Ukrainian tech repairing'])
    writer.writerow(['100001', 'CBS Python dev'])
    writer.writerow(['100002', 'Yemelianov Oleh Ukraine'])
    writer.writerow(['100003', 'Ivanov Dmytro Estonia'])
    writer.writerow(['100004', 'Sidorov Ivan Latvia'])