// Passo 1: Importe as partes do módulo que deseja utilizar 
import  {  MercadoPagoConfig ,  Payment  }  from  'mercadopago' ;

// Etapa 2: Inicializar o objeto cliente 
const  client  =  new  MercadoPagoConfig ( {  accessToken : 'APP_USR-7088407773309513-092312-59bbf54bf6a0f1aa0de3f73f6150ab60-444959623' ,  options : {  timeout : 5000 ,  idempotencyKey : 'abc'  }  } ) ;

// Etapa 3: Inicializar o objeto API 
const  payment  =  new  Payment ( client ) ;

// Etapa 4: Crie o objeto de solicitação 
const  body  =  { 
	transaction_amount : 12.34 , 
	description : '<DESCRIPTION>' , 
	payment_method_id : '<PAYMENT_METHOD_ID>' , 
	payer : { 
		email : '<Guuhaniceto@gmail.com>' 
	} , 
} ;

// Etapa 5: Criar objeto de opções de solicitação - Opcional 
const  requestOptions  =  { 
	idempotencyKey : '<IDEMPOTENCY_KEY>' , 
} ;

// Etapa 6: 
payment.create({ body }).then(console.log).catch(console.log);