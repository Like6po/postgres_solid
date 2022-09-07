from abc import ABC

from db.base import DB, SelectMixin, InsertMixin, DeleteMixin


class RedisBase(DB, SelectMixin, InsertMixin, DeleteMixin, ABC):
    pass
