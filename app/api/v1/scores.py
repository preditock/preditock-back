from fastapi import APIRouter

router = APIRouter()

@router.get("/scores", tags=["Scores"])
async def read_scores():

    return {"message": "All scores data"}

@router.get("/scores/{score_id}", tags=["Scores"])
async def read_scores(score_id: int):
    
    return {"message": f"Score data for {score_id}"}
