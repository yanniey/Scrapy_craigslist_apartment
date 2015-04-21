import json
import csv
from pprint import pprint


prices = []
with open('items.json') as data_file:
	data = json.load(data_file)

""" extract the price from each entry and put into a list """
for entry in data:
	prices.append(entry["price"])

""" calculate ave price """


print(str(prices))