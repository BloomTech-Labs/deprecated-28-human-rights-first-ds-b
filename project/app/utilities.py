from ast import literal_eval

import pandas as pd


def get_data():
    """ Sets up the data for api filtering """
    # leaving df_846 commented out for now, but did work
    # with routes when tested locally
    #df = pd.read_csv("df_846.csv")

    df = pd.read_csv("data.csv")
    
    #df_846 contains 'links' not 'src' column
    df["src"] = df["src"].apply(literal_eval)
    df["tags"] = df["tags"].apply(literal_eval)
    return df
