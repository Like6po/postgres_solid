from typing import Union

from pydantic import BaseModel


class Condition(BaseModel):
    name: str
    value: Union[str, int, bool]


class Data(BaseModel):
    name: str
    value: Union[str, int, bool]
