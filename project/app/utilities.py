from ast import literal_eval
import pandas as pd
from app.load import load_wrangle_data

def get_data():
    """ Sets up the data for api filtering """
    load_wrangle_data()
    df = pd.read_csv("app/df_846.csv")
    df["src"] = df["src"].apply(literal_eval)
    df["tags"] = df["tags"].apply(literal_eval)
    return df

