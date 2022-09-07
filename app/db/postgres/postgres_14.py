from typing import List, Union

from db.postgres.base import PG


class PG14(PG):
    def select(self, table: str, columns: List[str]) -> List[list]:
        return self.execute(f"""SELECT {', '.join([col for col in columns])} FROM {table}""",
                            fetchall=True)

    def insert(self, table: str, data: dict[str, Union[bool, str, int]]):
        return self.execute(
            f"""INSERT INTO {table} 
            ({', '.join(key for key in data.keys())}) 
            VALUES ({', '.join('%s' for _ in data.keys())})""",
            params=tuple(data.values()))

    def delete(self, table: str, conditions: dict[str, Union[bool, str, int]]):
        return self.execute(
            f"""DELETE FROM {table}
            WHERE {' AND '.join(f'{key}={val}' for key, val in conditions.items())}
            """
        )

    def update(self, table: str, data: dict[str, Union[bool, str, int]], conditions: dict[str, Union[bool, str, int]]):
        return self.execute(
            f"""UPDATE {table} 
            SET {', '.join(f'{key}=%s' for key in data.keys())} 
            WHERE {' AND '.join(f'{key}={val}' for key, val in conditions.items())}
            """,
            params=tuple(data.values())
        )
