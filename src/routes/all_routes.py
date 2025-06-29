from fastapi import APIRouter
from enum import Enum

from routes.routes import route_based


# preximo da api geral
class PrefixRouter(Enum):
    api = "/api/v1"


# tags da api home
class Tags(Enum):
    home = "Home"



routes_all = APIRouter()

# funcao centralizadora de rotas
def all_Rotes(app):
    app.include_router(route_based, prefix=PrefixRouter.api.value, tags=[Tags.home])



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