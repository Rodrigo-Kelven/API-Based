from fastapi import APIRouter
from payment.models import Carrinho
from payment.config import sdk


apiPayment = APIRouter()



@apiPayment.post("/criar_pagamento")
def criar_pagamento(carrinho: Carrinho):
    preference_data = {
        "items": [
            {
                "title": item.title,
                "quantity": item.quantity,
                "unit_price": item.unit_price,
                "currency_id": "BRL"
            }
	     for item in carrinho.items
        ],
        "back_urls": {
            "success": "https://www.exemplo.com/sucesso",
            "failure": "https://www.exemplo.com/falha",
            "pending": "https://www.exemplo.com/pendente"
        },
        "auto_return": "approved"
    }

    preference_response = sdk.preference().create(preference_data)

    print("DEBUG:", preference_response)

    if preference_response["status"] == 201:
        return {"init_point": preference_response["response"]["init_point"]}
    else:
        return {"erro": preference_response}
