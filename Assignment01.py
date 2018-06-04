import csv
import matplotlib.pyplot as plt

with open('machine_learning_1.csv') as csvfile:
    data = csv.reader(csvfile)



plt.plot(len(data[,21]), data[,21])

#readcsv('~/Users/annaleidbakker/Desktop/machine_learning_1.csv')
