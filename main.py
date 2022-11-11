import csv
import json
import datetime


def skip_x_element_in_list(lista, index_x):
    """Funkcja pomija kolumne C z danych wejsciowych"""
    lista_final = []

    for index, value in enumerate(lista):
        if index == index_x:
            continue
        else:
            lista_final.append(value)

    return lista_final

sciezka_raport = 'temperaturesDataRaportV2.pdf'
sciezka_dane = 'TemperaturesDataV2.csv'

# Data from CSV - Lists of Lists
with open(sciezka_dane, "r") as csvfile:
    data = list(csv.reader(csvfile))

#print('# Dane wejsciowe - {}'.format(data))

Iplist = []
for i in data:
    Iplist.append(i[1])

print(Iplist)


#element_0 = (data[0])
#print(element_0[0])

#print('# Report {} was generated!'.format(sciezka_raport))