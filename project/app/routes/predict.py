from fastapi import APIRouter

router = APIRouter()


@router.post("/predict/")
async def predict(text: str):
    """ Get prediction - placeholder """
    return {"result": text}
