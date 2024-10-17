import csv
import xml.etree.ElementTree as ET
import json

name = input('Input name:').title().strip()
surname = input('Input surname:').title().strip()
date_of_birth = input('Input date of birth in DD-MM-YY format:').strip()
city = input('Input city of living:').strip()


def write_to_csv():
    with open('data.csv', 'w', encoding='utf-8') as f:
        new_file = csv.writer(f, delimiter=';', quotechar='!')
        new_file.writerow([name, surname, date_of_birth, city])


def add_rows():
    with open('data.csv', 'a', newline= '', encoding='utf-8') as file:
        try:
            csv.writer(file).writerow([name, surname, date_of_birth, city])
        except TypeError:
            print('Unknown value. Try again.')


def convert_to_xml():
    root = ET.Element('root')
    data = ET.SubElement(root, 'data')
    new_l = [name, surname, date_of_birth, city]
    for info in new_l:
        ET.SubElement(data,'name\r').text = name
        ET.SubElement(data, 'surname\r').text = surname
        ET.SubElement(data, 'date_of_birth\r').text = date_of_birth
        ET.SubElement(data, 'city').text = city
    tree = ET.ElementTree(root)
    tree.write('data.xml')




def convert_to_json():
    data = [name, surname, date_of_birth, city]

    with open('data.json', 'w', encoding='utf-8') as j:
        json.dump(data, j, ensure_ascii=False)



def main():
    while True:
        print('1 - Make CSV file')
        print('2 - Add new rows to file')
        print('3 - Convert data to XML')
        print('4 - Convert data to json')
        print('5 - Exit program')
        print('--------------------------')
        action = int(input('What would you like to do:'))
        if action == 1:
            write_to_csv()
        elif action == 2:
            add_rows()
        elif action == 3:
            convert_to_xml()
        elif action == 4:
            convert_to_json()
        elif action == 5:
            print('Goodbye')
            break
        else:
            print('Unknown action. Try again.')
            continue

main()