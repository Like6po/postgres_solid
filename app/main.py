import os

from db.postgres.columns import Char, Int, Bool
from db.postgres.postgres_11 import PG11
from db.postgres.postgres_14 import PG14


def test_pg14():
    pg14 = PG14(host=os.getenv("DB_HOST_14"),
                port=os.getenv("DB_PORT"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                dbname=os.getenv("DB_NAME"))

    pg14.connect()
    try:
        # Тест подключения
        is_life = pg14.is_life()
        assert is_life == True

        # Создание тестовой таблицы
        pg14.create_table("test",
                          variables=[Int("identifier"),
                                     Char("name", max_length=64),
                                     Bool("is_active")])

        # Вставка элемента
        pg14.insert("test",
                    {"identifier": 1,
                     "name": "Ivan",
                     "is_active": True})

        result = pg14.select("test", ["*"])
        assert result == [[1, 'Ivan                                                            ', True]]

        # Обновление элемента
        pg14.update("test",
                    {"name": "Danya",
                     "is_active": False},
                    {"identifier": 1})
        result = pg14.select("test", ["*"])
        assert result == [[1, 'Danya                                                           ', False]]

        # Удаление элемента
        pg14.delete("test", {"identifier": 1})
        result = pg14.select("test", ["*"])
        assert result == []

    finally:
        pg14.disconnect()


def test_pg11():
    pg11 = PG11(host=os.getenv("DB_HOST_11"),
                port=os.getenv("DB_PORT"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                dbname=os.getenv("DB_NAME"))

    pg11.connect()
    try:
        # Тест подключения
        is_life = pg11.is_life()
        assert is_life == True

        # Создание тестовой таблицы
        pg11.create_table("test",
                          variables=[Int("identifier"),
                                     Char("name", max_length=64),
                                     Bool("is_active")])

        # Вставка элемента
        pg11.delete("test",
                    {"identifier": 1,
                     "name": "Ivan",
                     "is_active": True})

        result = pg11.select("test", ["*"])
        assert result == [[1, 'Ivan                                                            ', True]]

        # Обновление элемента
        pg11.update("test",
                    {"name": "Danya",
                     "is_active": False},
                    {"identifier": 1})
        result = pg11.select("test", ["*"])
        assert result == [[1, 'Danya                                                           ', False]]

        # Удаление элемента
        pg11.insert("test", {"identifier": 1})
        result = pg11.select("test", ["*"])
        assert result == []

    finally:
        pg11.disconnect()


def main():
    test_pg14()
    test_pg11()
    print("TEST OK :D")


if __name__ == "__main__":
    main()
