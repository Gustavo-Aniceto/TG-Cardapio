const express = require('express');
const mercadopago = require('mercadopago');

const app = express();

mercadopago.configure({
    access_token: 'APP_USR-7088407773309513-092312-59bbf54bf6a0f1aa0de3f73f6150ab60-444959623'
  });

// Rota para gerar o link de pagamento
app.get('/gerar-link-pagamento', async (req, res) => {
  let preference = {
    items: [
      {
        id: 'ribs-brisket-and-burnt-ends',
        title: "Joe's KC BBQ",
        unit_price: 110.99,
        quantity: 1,
        currency_id: 'BRL',
        picture_url: 'http://localhost:5500/img/cardapio/churrasco/joes-kc-ribs-brisket-and-burnt-ends.jpg',
      }
    ],
    back_urls: {
      success: 'http://127.0.0.1:5500/compracerta',
      failure: 'http://127.0.0.1:5500/compraerrada',
      pending: 'http://127.0.0.1:5500/compraerrada',
    },
    auto_return: 'approved',
  };

  try {
    const response = await mercadopago.preferences.create(preference);
    const linkPagamento = response.body.init_point;
    res.json({ link_pagamento: linkPagamento });
  } catch (error) {
    console.error(error);
    res.status(500).send('Erro ao criar preferência de pagamento');
  }
});

app.get('/compracerta', (req, res) => {
  res.send('Compra concluída com sucesso!');
});

app.get('/compraerrada', (req, res) => {
  res.send('A compra não foi realizada.');
});

app.listen(3000, () => {
  console.log('Servidor rodando na porta 3000');
});
