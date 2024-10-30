from datetime import datetime

from app.db.models.history import History
from pydantic import BaseModel

class HistoryDTO(BaseModel):
    idpessoa: int
    idfilme: int
    dtplay: datetime
    gostou: bool
    terminou: bool

    def __init__(self, idpessoa: int, idfilme: int, dtplay: datetime, gostou: bool, terminou: bool):
        super().__init__(idpessoa=idpessoa, idfilme=idfilme, dtplay=dtplay, gostou=gostou, terminou=terminou)

    def get_entity(self):
        entity = History()
        entity.id_pessoa = self.idpessoa
        entity.id_filme = self.idfilme
        entity.dt_play = self.dtplay
        entity.liked = self.gostou
        entity.finished = self.terminou
        return entity

    @staticmethod
    def from_entity(entity: History):
        history_dto = HistoryDTO(entity.id_pessoa, entity.id_filme, entity.dt_play, entity.liked, entity.finished)
        return history_dto