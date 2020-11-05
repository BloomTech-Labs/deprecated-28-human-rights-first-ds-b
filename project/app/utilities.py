from ast import literal_eval

import pandas as pd


def get_data():
    """ Sets up the data for api filtering """
    df = pd.read_csv("app/data.csv")
    df["src"] = df["src"].apply(literal_eval)
    df["tags"] = df["tags"].apply(literal_eval)
    return df
