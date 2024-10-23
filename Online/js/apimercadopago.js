const express = require('express');
const mercadopago = require('mercadopago');
const app = express();

// Configuração da chave do Mercado Pago (Access Token)
mercadopago.configurations.setAccessToken('APP_USR-7088407773309513-092312-59bbf54bf6a0f1aa0de3f73f6150ab60-444959623');

// Middleware para aceitar JSON
app.use(express.json());

app.post('/process_payment', async (req, res) => {
    const paymentData = {
        transaction_amount: Number(req.body.transactionAmount),
        token: req.body.token,
        description: 'Descrição do pagamento',
        installments: Number(req.body.installments),
        payment_method_id: req.body.paymentMethodId,
        payer: {
            email: req.body.payer.email,
            identification: {
                type: req.body.payer.identification.type,
                number: req.body.payer.identification.number,
            },
        },
    };

    try {
        const payment = await mercadopago.payment.save(paymentData);
        res.status(200).json(payment);
    } catch (error) {
        console.error('Erro ao processar pagamento:', error);
        res.status(500).send(error);
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
