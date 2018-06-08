



import csv
import pandas as pd
from numpy import genfromtxt

test = pd.read_csv("csv-participant-one/heart_rate_smartwatch.csv", index_col = False, header=0)
# Simple class to impute missing values of a single columns.
print(test)
class ImputationMissingValues:

    # Impute the mean values in case if missing data.
    def impute_mean(self, dataset, col):
        dataset[col] = dataset[col].fillna(dataset[col].mean())
        return dataset

    # Impute the median values in case if missing data.
    def impute_median(self, dataset, col):
        dataset[col] = dataset[col].fillna(dataset[col].median())
        return dataset

    # Interpolate the dataset based on previous/next values..
    def impute_interpolate(self, dataset, col):
        dataset[col] = dataset[col].interpolate()
        # And fill the initial data points if needed:
        dataset[col] = dataset[col].fillna(method='bfill')
        return dataset