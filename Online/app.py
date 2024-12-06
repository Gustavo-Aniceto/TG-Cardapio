from flask import Flask, jsonify
from flask_cors import CORS
import mercadopago

app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5500'])

@app.route('/gerar-link-pagamento', methods=['GET'])
def gerar_link_pagamento():
    sdk = mercadopago.SDK("APP_USR-6594311902089290-120516-fc10c46b889259df2a4fb4708f3c5567-444959623")
    payment_data = {
        "items": [
            {
                "id": "shake-shack-shackburger-8-pack",
                "title": "Shake Shack",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 99.00,
            },
            {
                "id": "ribs-brisket-and-burnt-ends",
                "title": "Joe's KC BBQ",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 110.99,
            },
            {
                "id": "005-kings-carolina-oink-sampler",
                "title": "Kings BBQ",
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": 89,
            },
            {
                "id": "whole-brisket-texas-bbq-sauce",
                "title": "Franklin Barbecue",
                "unit_price": 249,
                "quantity": 1,
                "currency_id": "BRL",
            },
                        {
                "id": "whole-texas-smoked-brisket",
                "title": "Terry Black's Barbecue",
                "unit_price": 189,
                "quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": "mini-trinity-bbq-combo-brisket-ribs-and-links",
                "title": "Bludso's BBQ",
                "unit_price": 139,
                "quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": "235203-blue-smoke-baby-back-ribs-backyard-barbecue-chicken-combo",
                "title": "Blue Smoke",
                "unit_price": 129,
                "quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": "006-kings-meat-lovers-special",
                "title": "Kings BBQ",
                "unit_price": 139,
                "quantity": 1,
               " currency_id": "BRL",
            },
            {
                "id": "the-big-ugly-bbq-dinner-for-6",
               " title": "Ugly Drum",
               " unit_price": 229,
               " quantity": 1,
               " currency_id": "BRL",
            },
            {
                "id": "17796-mighty-quinns-bbq-sampler-pack",
                "title": "Mighty Quinn's BBQ",
                "unit_price": 169,
               " quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": "post-oak-smoked-half-brisket",
                "title": "Southside Market & Barbeque",
                "unit_price": 109,
                "quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": "best-of-texas-bbq-combo-serves-14",
                "title": "Snow's BBQ",
                "unit_price": 269,
                "quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": 'the-gramercy-tavern-burger-4-pack',
                "title": "Gramercy Tavern",
                "unit_price": 99,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": 'shake-shack-shackburger-8-pack',
                "title": "Shake Shack",
                "unit_price": 49,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": 'gotts-cheeseburger-kit-for-4',
                "title": "Gott's Roadside",
                "unit_price": 99,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": 'le-big-matt-kit-for-6',
                "title": "Emmy Squared",
                "unit_price": 99,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": 'shake-shack-shackburger-16-pack',
                "title": "Shake Shack",
                "unit_price": 89,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": '21-usda-prime-burgers-pack-of-18-8oz-each',
              "  title": "Peter Luger k House",
                "unit_price": 175.95,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": 'double-stack-burger-kit-for-4',
                "title": "Holeman & Finch",
                "unit_price": 79,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": 'goldbelly-burger-bash-pack',
                "title": "Pat LaFrieda Meats",
                "unit_price": 109,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
               " id": 'burger-au-poivre-kit-4-pack',
                "title": "Raoul's",
                "unit_price": 99,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
               " id": 'goldbelly-burger-blend-4-lbs',
                "title": "Flannery Beef",
                "unit_price": 79,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": 'gotts-complete-cheeseburger-kit-for-8',
               " title": "Gott's Roadside",
                "unit_price": 149,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": "Feijoada Completa",
                "title": "Feijoada Completa",
                "unit_price": 80,
                "quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": "Curau de Milho",
                "title": "Curau de Milho",
                "unit_price": 30,
                "quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": "Tambaqui assado",
                "title": "Tambaqui assado",
                "unit_price": 100,
                "quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": "Moqueca de peixe",
                "title": "Moqueca de peixe",
                "unit_price": 120,
                "quantity": 1,
               " currency_id": "BRL",
            },
            {
                "id": "Pato no Tucupi",
               " title": "Pato no Tucupi",
               " unit_price": 119,
               " quantity": 1,
               " currency_id": "BRL",
            },
            {
                "id": "Galinhada com pequi",
                "title": "Galinhada com pequi",
                "unit_price": 150,
               " quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": "Vaca Atolada",
                "title": "Vaca Atolada",
                "unit_price": 130,
                "quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": "Acarajé",
                "title": "Acarajé",
                "unit_price": 99,
                "quantity": 1,
                "currency_id": "BRL",
            },
            {
                "id": 'Maria Isabel',
                "title": "Maria Isabel",
                "unit_price": 39,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": 'Tacacá',
                "title": "Tacacá",
                "unit_price": 225,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": 'Contra File',
                "title": "Contra File",
                "unit_price": 40,
                "quantity": 1,
                "currency_id": 'BRL',
            },
            {
                "id": 'Costela',
                "title": "Costela",
                "unit_price": 165,
                "quantity": 1,
                "currency_id": 'BRL',
            }

            
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
