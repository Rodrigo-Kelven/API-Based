from fastapi import APIRouter, Depends, HTTPException, Request, Response, status, Query
from fastapi_limiter.depends import RateLimiter
from typing import List
from config.config import lifespan

route_based = APIRouter()


@route_based.get(
    path='/test',
    status_code=status.HTTP_200_OK,
    description="Route Home",
    name="Route Name"
)
async def routeHome():
    return {"Hello Word"}


@route_based.get(
    path="/",
    status_code=status.HTTP_200_OK,
    description="Rota sem limit de requisicoes",
    name="Route no limit request",
    response_description="No Limit Request"
)
async def index():
    return {"msg": "This endpoint has no limits."}

@route_based.get(
    path="/search",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(RateLimiter(times=2, seconds=5))],
    description="Rota com limit de requisicoes",
    name="Route with limit request",
    response_description="With Limit Request"
)
async def search_handler():
    return {"msg": "This endpoint has a rate limit of 2 requests per 5 seconds."}

@route_based.get(
    path="/upload",
    dependencies=[Depends(RateLimiter(times=3, seconds=10))],
    description="Rota com limit de requisicoes",
    name="Route with limit request",
    response_description="With Limit Request"
)
async def upload_handler():
    return {"msg": "This endpoint has a rate limit of 2 requests per 10 seconds."}


# Simulando uma lista de itens
items = [{"item_id": i, "name": f"Item {i}"} for i in range(1, 101)]  # 100 itens

@route_based.get(
    path="/items/",
    response_model=List[dict],
    description="Rota com pagination",
    name="Route with pagination",
    response_description="With Pagination"
)
async def get_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, gt=0)
):
    """
    Retorna uma lista de itens com paginação.
    - **skip**: Número de itens a serem pulados (offset).
    - **limit**: Número máximo de itens a serem retornados.
    """
    return items[skip: skip + limit]