import csv

names = []

with open("data.csv", newline = '') as csvfile:
    reader = csv.reader(csvfile)
    first_row = next(reader)
    names = str(first_row).split(';')

l_names = []

for name in names:
    wo_conf = str(name).split('(')[1]
    clean = wo_conf.split(')')[0]
    l_names.append(clean)

from collections import  Counter

winner = str(Counter(l_names)).split(',')[0]
winner = winner.split('{')[1]
print("Ex2: The winner is " + winner + " appearances")


import pandas

python_mails = []

df = pandas.read_csv("data.csv", sep = ';', header=None)
for series in df:
    list = df[series].tolist()
    if "Python" in list[0]:
        for field in list[1:]:
            name = str(field)
            name = name.split('/')[0]
            if name != 'nan':
                python_mails.append(name)

wo_duplicates = set(python_mails)
print("Ex3: Number of non-duplicate names equals " + str(len(wo_duplicates)))

earnings = {}

for name in l_names:
    earnings[name] = 0

for series in df:
    list = df[series].tolist()
    list[0] = str(list[0]).split('(')[1]
    list[0] = list[0].split(')')[0]
    col_sum = 0
    for field in list[1:]:
        money = str(field)
        if money != 'nan':
            money = money.split('/')[1]
            money = int(money)
            col_sum += money
    earnings[list[0]] += col_sum

best = max(earnings, key=earnings.get)
print("Ex4: Most earnings from: " + str(best) + ": " + str(earnings[best]))

countries = []

for series in df:
    list = df[series].tolist()
    for field in list[1:]:
        field = str(field)
        if field != 'nan':
            country = field.split('.')[1]
            country = country.split('/')[0]
            countries.append(country)

countries_wo_dup = set(countries)
earnings_per_country = {}

for c in countries_wo_dup:
    earnings_per_country[c] = 0

for series in df:
    list = df[series].tolist()
    for field in list[1:]:
        field = str(field)
        if field != 'nan':
            country = field.split('.')[1]
            country, money = country.split('/')
            earnings_per_country[country] += int(money)

best_c = max(earnings_per_country, key=earnings_per_country.get)
print("Ex5: Most earnings from: " + str(best_c) + ": " + str(earnings_per_country[best_c]))