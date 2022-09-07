from abc import abstractmethod, ABC


class DB(ABC):
    def __init__(self):
        self.con = None

    @abstractmethod
    def connect(self):
        """
        Method to create connection to DB
        """
        raise NotImplementedError

    @abstractmethod
    def disconnect(self):
        """
        Method to close connection to DB
        """
        raise NotImplementedError

    @abstractmethod
    def is_life(self) -> bool:
        """
        Method return True, if connection active
        """
        raise NotImplementedError

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Method to execute statements
        """
        raise NotImplementedError


class TableCreateMixin(ABC):
    @abstractmethod
    def create_table(self, *args, **kwargs):
        """
        Method to create table in DB
        """
        raise NotImplementedError


class InsertMixin(ABC):
    @abstractmethod
    def insert(self, *args, **kwargs):
        """
        Method to insert data in DB
        """
        raise NotImplementedError


class SelectMixin(ABC):
    @abstractmethod
    def select(self, *args, **kwargs):
        """
        Method to select data from DB
        """
        raise NotImplementedError


class UpdateMixin(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        """
        Method to update data in DB
        """
        raise NotImplementedError


class DeleteMixin(ABC):
    @abstractmethod
    def delete(self, *args, **kwargs):
        """
        Method to delete data from DB
        """
        raise NotImplementedError
