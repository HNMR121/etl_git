
import  csv
from pprint import pprint
import json

data = open('ReportInvoiceLines.csv')

def output_json():
    content = json.dumps([row for row in reader], ensure_ascii=False)#.encode('windows-1251')
    # print(content)
    with open('data.json', 'w') as file:
        file.write(content)

with open('ReportInvoiceLines2.csv', 'r', encoding="utf-8-sig") as data:

    reader = csv.DictReader(data, delimiter=',')

    # for row in reader:
        # print(row)
    #     print(row)
    # for row in data:
    #     print(row)
    output_json()
