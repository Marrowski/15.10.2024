from xml.etree import ElementTree as ET

tree = ET.parse('task2.xml')
root = tree.getroot()

for data in root:
    print('PK: ', (data.attrib, data.get('pk')))
    print('{} {} {}'.format(
        data.find('.products/product/name').text,
        data.find('.products/product/price').text,
        data.find('./shipping_type').text
    ))

name = root.findall('.customer/name')
surname = root.findall('.customer')
contact_info = root.findall('.contact/phone')

for val in zip(name, surname, contact_info):
    row = {val.tag: val.text for i in val}
    print(row)

for data in root:
    print('PK: ', data.attrib)
    for j in data:
        print('{}: {}'.format(j.tag, j.text))