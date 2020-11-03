from fastapi import APIRouter
import json

from app.utilities import get_data


router = APIRouter()
DF = get_data()  # Global Data Source - pd.DataFrame


@router.get('/report-by-id/')
async def report_by_id(idx: str):
    """ Get report by id """
    result = DF.iloc[int(idx)].to_json(orient="index")
    return json.loads(result)


@router.get('/report-by-city/')
async def report_by_city(city: str):
    """ Get report by city """
    result = DF[DF['city'] == city].to_json(orient="index")
    return json.loads(result)


@router.get('/report-by-state/')
async def report_by_state(state: str):
    """ Get report by state """
    result = DF[DF['state'] == state].to_json(orient="index")
    return json.loads(result)
