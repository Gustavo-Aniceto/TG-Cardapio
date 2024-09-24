import mercadopago

# Instanciar o SDK com a chave de acesso
sdk = mercadopago.SDK("APP_USR-7088407773309513-092312-59bbf54bf6a0f1aa0de3f73f6150ab60-444959623")

# Configurar opções de requisição
request_options = mercadopago.config.RequestOptions()
request_options.custom_headers = {
    'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
}

# Dados de pagamento
payment_data = {
    "items": [
        {
            "id": "ribs-brisket-and-burnt-ends",
            "picture_url": "./img/cardapio/churrasco/joes-kc-ribs-brisket-and-burnt-ends.6710e994980e485e6441b794717ad6fb.jpg",
            "title": "Joe's KC BBQ",
            "unit_price": 110.99,
            "quantity": 1,
            "currency_id": "BRL"
        }
    ]
}

# Criar preferência de pagamento
result = sdk.preference().create(payment_data, request_options)

# Obter a resposta
payment = result["response"]

# Exibir a resposta
print(payment)
