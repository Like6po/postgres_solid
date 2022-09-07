from abc import abstractmethod, ABC


class DB(ABC):
    def __init__(self):
        self.con = None

    @abstractmethod
    def connect(self):
        raise NotImplementedError

    @abstractmethod
    def disconnect(self):
        raise NotImplementedError

    @abstractmethod
    def is_life(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError


class TableCreateMixin(ABC):
    @abstractmethod
    def create_table(self, *args, **kwargs):
        raise NotImplementedError


class InsertMixin(ABC):
    @abstractmethod
    def insert(self, *args, **kwargs):
        raise NotImplementedError


class SelectMixin(ABC):
    @abstractmethod
    def select(self, *args, **kwargs):
        raise NotImplementedError


class UpdateMixin(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        raise NotImplementedError


class DeleteMixin(ABC):
    @abstractmethod
    def delete(self, *args, **kwargs):
        raise NotImplementedError
