import csv

f = open("data/txt_ldc.txt", "w")

with open('data/ldc_to_export.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        f.write(str(row))

f.close()