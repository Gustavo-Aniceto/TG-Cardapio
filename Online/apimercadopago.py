import mercadopago

sdk = mercadopago.SDK("APP_USR-7088407773309513-092312-59bbf54bf6a0f1aa0de3f73f6150ab60-444959623")

request_options = mercadopago.config.RequestOptions()
request_options.custom_headers = {
    'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
}

payment_data = {
    "items": [
        {"id": "ribs-brisket-and-burnt-ends","img": "./img/cardapio/churrasco/joes-kc-ribs-brisket-and-burnt-ends.6710e994980e485e6441b794717ad6fb.jpg","title": "Joe's KC BBQ","unit_price": 110.99"Currency_id":"BRL"}
    ]
}
result = sdk.preference().create(payment_data, request_options)
payment = result["response"]

print(payment)