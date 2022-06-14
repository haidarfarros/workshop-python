import csv
import urllib.request

url = ("https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv")
response = urllib.request.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print(row)