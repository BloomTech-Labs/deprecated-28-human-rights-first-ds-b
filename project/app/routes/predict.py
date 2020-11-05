import joblib
from fastapi import APIRouter

from app.routes.model import TextMatcher

router = APIRouter()
model: TextMatcher = joblib.load('app/model.joblib')


@router.post("/predict/")
async def predict(text: str):
    """ Get ranked prediction """
    return {"result": model(text)}
