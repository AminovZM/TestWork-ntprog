from datetime import datetime
from pydantic import BaseModel


class BasketApplication(BaseModel):
    creation_time: datetime
    change_time: datetime
    status: str
    side: str
    price: int
    amount: int
    instrument: str


