
import  csv
from pprint import pprint
import json


def output_xml():
    xml = ['<?xml version="1.0" encoding="utf-8"?>']
    for row in reader:
        xml.append("<bank>")

        xml.append("</bank>")

with open('ReportInvoiceLines2.csv', 'r', encoding="utf-8-sig") as data:

    reader = csv.DictReader(data, delimiter=',')

    output_json()
