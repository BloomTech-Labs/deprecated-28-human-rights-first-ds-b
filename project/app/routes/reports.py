import json

from pandas import DataFrame
from fastapi import APIRouter

from app.utilities import get_data

router = APIRouter()
DF: DataFrame = get_data()  # Global Data Source


@router.get("/report-by-id/")
async def report_by_id(idx: str):
    """ Get report by id number
    returns a single report as JSON object """
    result = DF.iloc[int(idx)].to_json(orient="index")
    return json.loads(result)


@router.get("/report-by-city/")
async def report_by_city(city: str):
    """ Get reports by city name
    returns a list of reports as JSON objects """
    result = DF[DF["city"] == city.title()].to_json(orient="records")
    return json.loads(result)


@router.get("/report-by-state/")
async def report_by_state(state: str):
    """ Get reports by state name
    returns a list of reports as JSON objects """
    result = DF[DF["state"] == state.title()].to_json(orient="records")
    return json.loads(result)


@router.get("/full-report/")
async def full_report():
    """ Get all reports
    returns a list of reports as JSON objects """
    result = DF.to_json(orient="records")
    return json.loads(result)
