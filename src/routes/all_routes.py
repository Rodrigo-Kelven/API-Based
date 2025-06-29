from fastapi import APIRouter
from enum import Enum

from routes.routes import route_based
from payment.routes import apiPayment

# preximo da api geral
class PrefixRouter(Enum):
    api = "/api/v1"
    paymente = "/api/vi/payment"

# tags da api home
class Tags(Enum):
    home = "Home"
    paymente = "API Payment"


routes_all = APIRouter()

# funcao centralizadora de rotas
def all_Rotes(app):
    app.include_router(route_based, prefix=PrefixRouter.api.value, tags=[Tags.home])
    app.include_router(apiPayment, prefix=PrefixRouter.paymente.value, tags=[Tags.paymente])


# atalho
"""
include_router(
    router: APIRouter,
    *,
    prefix: str = "",
    tags: List[str | Enum] | None = None,
    dependencies: Sequence[Depends] | None = None,
    responses: Dict[int | str, Dict[str, Any]] | None = None,
    deprecated: bool | None = None,
    include_in_schema: bool = True,
    default_response_class: type[Response] = Default(JSONResponse),
    callbacks: List[BaseRoute] | None = None,
    generate_unique_id_function: (APIRoute) -> str = Default(generate_unique_id)
) -> None
"""