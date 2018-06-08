##import libraries
import csv
import matplotlib.pyplot as plt



with open(".csv", 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimter= ' ', quotechar = '|')
    for row in spamreader:
    print ', '.join(row)



