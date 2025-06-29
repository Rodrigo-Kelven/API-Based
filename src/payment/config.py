import os
from dotenv import load_dotenv
import mercadopago

# Carrega as variáveis do .env
load_dotenv()

# Obtém o token do ambiente
ACCESS_TOKEN = os.getenv("MERCADO_PAGO_ACCESS_TOKEN")

# Inicializa o SDK
sdk = mercadopago.SDK(ACCESS_TOKEN)
print("TOKEN CARREGADO:", ACCESS_TOKEN)

