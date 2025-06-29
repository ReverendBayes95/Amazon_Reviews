import pandas as pd


def read_reviews(path, colnames):

    return pd.read_csv(path, names = colnames)