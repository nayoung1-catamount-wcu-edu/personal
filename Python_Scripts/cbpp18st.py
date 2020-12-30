# Imports
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import requests
import numpy as np
import seaborn as sns


def cbpp18st(zipfile, filenum):
    """
    input:
        zipfile : str : path to zip folder
        filenum : int : file in folder
    output:
        pairplot : visual analysis of data
    """
    response = requests.get(zipfile)
    zip_file = ZipFile(BytesIO(response.content))
    files = zip_file.namelist()
    for file in files:
        with zip_file.open(files[filenum]) as csvfile:
            df = pd.read_csv(csvfile, encoding="ISO-8859-1",
                             sep=",", skiprows=9)

            # Remove nan and fill future column names
            df.dropna(axis=1, thresh=15, inplace=True)
            df = df.ffill(axis=1)

            # Create column names by adding two rows together
            df.iloc[0] = df.iloc[0] + " " + df.iloc[1]

            # Set first row as header
            new_header = df.iloc[0]
            df = df[1:]
            df.columns = new_header

            # Drop any nan values left over
            df.dropna(inplace=True)

            # Replace nan in column header
            df.columns.values[[0, 1]] = [
                "Demographic",
                "U.S. population age 16 or older",
            ]

            # Add date value
            df["Year"] = 2018

            # Strip symbols from Demographic column
            df["Demographic"] = df["Demographic"].str.replace("*", "")
            df["Demographic"] = df["Demographic"].str.replace("/a", "")
            df["Demographic"] = df["Demographic"].str.replace(",b", "")

            # Drop Total row
            df = df.drop(2)

            # Set index
            df.set_index(df["Demographic"], inplace=True)
            df.drop("Demographic", axis=1, inplace=True)

            # clean columns and change dtypes
            for c in df.columns:
                if "Percent" in c:
                    df[c] = df[c].astype(float)
                elif "Number" in c:
                    df[c] = df[c].str.replace(",", "").astype(int)

    return sns.pairplot(df, hue="Year")
