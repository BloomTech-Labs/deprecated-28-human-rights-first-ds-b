from ast import literal_eval

from fastapi import APIRouter
import pandas as pd

router = APIRouter()


@router.get('/getdata')
async def getdata():
    """ Get dataset in JSON format """
    # df = pd.read_csv('data.csv')
    # df['src'] = df['src'].apply(literal_eval)
    # df['tags'] = df['tags'].apply(literal_eval)
    # return df.to_json(orient="records")
    return {"Result": "Hello from AWS"}
