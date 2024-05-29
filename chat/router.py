from fastapi import APIRouter, Depends, Query
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


@router.get("/")
async def get_applications(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max number of items to return"),
    session: AsyncSession = Depends(get_async_session)
):
    query = select(application).offset(skip).limit(limit)
    result = await session.execute(query)

    rows_as_dicts = [row._asdict() for row in result.all()]

    return rows_as_dicts
