from typing import List

from db.postgres.base import PG
from db.postgres.schemas import Condition, Data


class PG14(PG):
    def select(self, table: str, columns: List[str]) -> List[list]:
        return self.execute(f"""SELECT {', '.join([col for col in columns])} FROM {table}""",
                            fetchall=True)

    def insert(self, table: str, data: List[Data]):
        return self.execute(
            f"""INSERT INTO {table} 
            ({', '.join(d.name for d in data)}) 
            VALUES ({', '.join('%s' for _ in data)})""",
            params=tuple(d.value for d in data))

    def delete(self, table: str, conditions: List[Condition]):
        return self.execute(
            f"""DELETE FROM {table}
            WHERE {' AND '.join(f'{c.name}={c.value}' for c in conditions)}
            """
        )

    def update(self, table: str, data: List[Data], conditions: List[Condition]):
        return self.execute(
            f"""UPDATE {table} 
            SET {', '.join(f'{d.name}=%s' for d in data)} 
            WHERE {' AND '.join(f'{c.name}={c.value}' for c in conditions)}
            """,
            params=tuple(d.value for d in data)
        )
