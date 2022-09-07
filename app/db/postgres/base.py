from abc import ABC, abstractmethod
from typing import List, Union

import psycopg2
from psycopg2.extras import DictCursor

from db.base import DB, TableCreateMixin, SelectMixin, InsertMixin, UpdateMixin, DeleteMixin
from db.postgres.columns import Int, Char, Bool


class PGBase(DB, TableCreateMixin, SelectMixin, InsertMixin, UpdateMixin, DeleteMixin, ABC):
    pass


class PG(PGBase, ABC):
    def __init__(self, host: str,
                 port: str,
                 password: str,
                 user: str,
                 dbname: str):
        super().__init__()
        self.host = host
        self.port = port
        self.password = password
        self.user = user
        self.dbname = dbname

    def connect(self):
        self.con = psycopg2.connect(dbname=self.dbname,
                                    user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    port=self.port)
        return self.con

    def disconnect(self):
        self.con.close()

    def execute(self, statement: str, params: tuple = (),
                fetchall: bool = False, fetchone: bool = False):
        with self.con.cursor(cursor_factory=DictCursor) as cursor:
            cursor: DictCursor
            try:
                cursor.execute(statement, params)
                if fetchall:
                    return cursor.fetchall()
                elif fetchone:
                    return cursor.fetchone()
                return
            except psycopg2.Error:
                raise

    def is_life(self) -> bool:
        return bool(self.execute("SELECT 1",
                                 fetchone=True))

    def create_table(self, name: str, variables: List[Union[Int, Char, Bool]]):
        with self.con.cursor(cursor_factory=DictCursor) as cursor:
            cursor: DictCursor
            cursor.execute(
                f"""CREATE TABLE {name} ({','.join(f'{var.as_sql()}' for var in variables)})
                """
            )
            return 1

    @abstractmethod
    def select(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def insert(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update(self, *args, **kwargs):
        raise NotImplementedError
