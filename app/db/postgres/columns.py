from abc import ABC, abstractmethod


class ColumnType(ABC):
    data_type = None

    @abstractmethod
    def __init__(self, name: str, **kwargs):
        if not self.data_type:
            raise NotImplementedError
        self.data = {"type": self.data_type, "name": name}

    @abstractmethod
    def as_sql(self):
        raise NotImplementedError


class Bool(ColumnType):
    data_type = "bool"

    def __init__(self, name: str):
        super().__init__(name)

    def as_sql(self):
        return f"{self.data['name']} {self.data['type']}"


class Int(ColumnType):
    data_type = "integer"

    def __init__(self, name: str):
        super().__init__(name)

    def as_sql(self):
        return f"{self.data['name']} {self.data['type']}"


class Char(ColumnType):
    data_type = "char"

    def __init__(self, name: str, max_length: int):
        super().__init__(name)
        self.data.update({"max_length": max_length})

    def as_sql(self):
        return f"{self.data['name']} {self.data['type']}({self.data['max_length']})"
