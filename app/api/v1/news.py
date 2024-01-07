from fastapi import APIRouter

router = APIRouter()

@router.get("/news", tags=["News"])
async def read_news():

    return {"message": "All news data"}

@router.get("/news/{news_id}", tags=["News"])
async def read_news(news_id: int):

    return {"message": f"News data for {news_id}"}

