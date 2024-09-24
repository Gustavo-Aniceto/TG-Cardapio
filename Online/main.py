from flask import flask, render_template # type: ignore
from apimercadopago import gerar_link_pagamento

app = flask(__name__)

@app.route("/")
def homepage():
    link_iniciar_pagamento = gerar_link_pagamento()
    return render_template("index.html", link_pagamento=link_iniciar_pagamento)

@app.route("/compracerta")
def compra_certa():
    return render_template("compracerta.html")

@app.route("/compraerrada")
def compra_errada():
    return render_template("compraerrada.html")

if __name__=="__main__":
    app.run()
