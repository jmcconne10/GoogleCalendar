
import csv
import pandas as pd

#with open('temp.csv', 'r') as csv_file:
reader = pd.read_csv("testCalendar.csv")

for index, row in reader.iterrows():
    #print(row.values)
    print("Date:" + row['Date'] + " Time:" + row['Time'] + " Event: " + row['Event'])

