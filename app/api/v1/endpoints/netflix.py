from fastapi import APIRouter, Depends
from app.api.dto.history_dto import HistoryDTO
from app.service.netflix_service import NetflixService

router = APIRouter()

@router.get("/catalog")
async def get_catalog(service: NetflixService = Depends()):
    return await service.get_catalog()

@router.get("/history/user/{user_id}")
async def get_user_history(user_id: int, service: NetflixService = Depends()):
    return service.get_user_history(user_id)

@router.get("/best")
async def get_liked_finalized(service: NetflixService = Depends()):
    return service.get_liked_finalized()

@router.post("")
async def save(history: HistoryDTO ,service: NetflixService = Depends()):
    return service.save(history)