const { MongoClient } = require('mongodb');
const uri = "mongodb+srv://guuhaniceto:<db_password>@cluster0.bv2bo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";
const client = new MongoClient(uri);

async function conectar() {
    try {
        await client.connect();
        console.log('Conectado ao MongoDB Atlas');
    } catch (error) {
        console.error('Erro de conexão:', error);
    } finally {
        await client.close();
    }
}

conectar();
