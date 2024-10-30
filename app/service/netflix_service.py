from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.api.dto.filme_dto import Filmes
from app.db.session import get_db
from app.db.models.history import History
from app.api.dto.history_dto import HistoryDTO
from app.service.oauth_service import OAuthService
from app.config.settings import Settings
import httpx

settings = Settings()

class NetflixService:
    def __init__(self, db: Session = Depends(get_db), oauth_service: OAuthService = Depends()):
        self.db = db
        self.oauth_service = oauth_service

    async def get_catalog(self):
        async with httpx.AsyncClient() as client:
            access_token = await self.oauth_service.get_token()
            if access_token is not None:
                header = {
                    'Authorization': access_token
                }
                url = settings.service_endpoint_filme_getall
                response = await client.get(url, headers=header)
                data = response.json()
                return Filmes(filmes = data)

    def get_user_history(self, user_id: int):
        histories = self.db.query(History).filter(History.id_pessoa == user_id).all()

        history_dto_list = list()
        for history in histories:
            history_dto_list.append(HistoryDTO.from_entity(history))

        return history_dto_list

    def get_liked_finalized(self):
        tablename = History.__tablename__
        schema = History.__table_args__['schema']
        sql_query = text(f"SELECT * FROM {schema}.{tablename} WHERE gostou = :gostou AND  terminou = :terminou")

        result = self.db.execute(sql_query, {"gostou": True, "terminou": True})
        return [HistoryDTO(**row) for row in result.mappings()]

    def save(self, history_dto: HistoryDTO):
        history = history_dto.get_entity()
        self.db.add(history)
        self.db.commit()

        return self.get_user_history(history_dto.idpessoa)