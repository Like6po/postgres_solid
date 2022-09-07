from abc import ABC

from db.base import DB, SelectMixin, InsertMixin, UpdateMixin, DeleteMixin


class MongoBase(DB, SelectMixin, InsertMixin, UpdateMixin, DeleteMixin, ABC):
    pass
