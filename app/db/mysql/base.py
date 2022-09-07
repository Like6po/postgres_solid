from abc import ABC

from db.base import DB, TableCreateMixin, SelectMixin, InsertMixin, UpdateMixin, DeleteMixin


class MySQLBase(DB, TableCreateMixin, SelectMixin, InsertMixin, UpdateMixin, DeleteMixin, ABC):
    pass
