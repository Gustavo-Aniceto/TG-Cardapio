from flask import Flask, jsonify
from flask_cors import CORS
import mercadopago

app = Flask(__name__)
CORS(app)  # Permite CORS para todas as rotas

@app.route('/gerar-link-pagamento', methods=['GET'])
def gerar_link_pagamento():
    sdk = mercadopago.SDK("APP_USR-7088407773309513-092312-59bbf54bf6a0f1aa0de3f73f6150ab60-444959623")
    payment_data = {
        "items": [
            {
                "id": "shake-shack-shackburger-8-pack",
                "title": "Shake Shack",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 49.00,
            },
        ],
        "back_urls": {
            "success": "http://127.0.0.1:5500/Online/compracerta.html",
            "failure": "http://127.0.0.1:5500/Online/compraerrada.html",
            "pending": "http://127.0.0.1:5500/Online/compraerrada.html",
        },
        "auto_return": "all",
    }
    result = sdk.preference().create(payment_data)
    payment = result["response"]
    link_iniciar_pagamento = payment["sandbox_init_point"]
    return jsonify({"link": link_iniciar_pagamento})

if __name__ == "__main__":
    app.run(debug=True)
