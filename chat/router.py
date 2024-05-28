from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from chat.schemas import BasketApplication
from chat.models import application

from database import get_async_session


router = APIRouter(
    prefix="/applications",
    tags=["Application"]
)


@router.post("/")
async def add_applications(new_product: BasketApplication, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(application).values(**new_product.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}