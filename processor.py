import pandas as pd
import PyPDF2


def preprocess(data):

  
    # We will remove unwanted columns from this dataset
    data.dropna( axis=1, inplace=True)
    # we will Removing rows having null value.
    data.dropna(inplace=True)

    return data