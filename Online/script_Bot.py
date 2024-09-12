import telebot  # type: ignore
from telebot import types  # type: ignore
from datetime import datetime
import uuid
import qrcode
import io

# Token do seu bot
TOKEN_BOT = "7152044356:AAF0SjFkBUH0ecGs-RUmWur5Ih_lNnRnvHw"

# Inicialização do bot
bot = telebot.TeleBot(TOKEN_BOT)

# Dicionário para armazenar os dados do usuário durante a conversa
dados_usuario = {}

# Função para determinar a saudação com base na hora
def obter_saudacao(hora):
    if 8 <= hora < 12:
        return "Bom dia"
    elif 12 <= hora < 19:
        return "Boa tarde"
    else:
        return "Boa noite"

# Função para enviar mensagem de boas-vindas
def enviar_mensagem_boas_vindas(chat_id, nome_usuario, saudacao):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Pagamento', callback_data='pagamento')
    btn2 = types.InlineKeyboardButton(text='Voltar ao cardápio', callback_data='voltarCardapio')
    btn3 = types.InlineKeyboardButton(text='Chamar Garçom', callback_data='chamarGarçom')
    btn4 = types.InlineKeyboardButton(text='Cancelar Pedido', callback_data='cancelarPedido')
    markup.add(btn1, btn2, btn3, btn4)
    
    mensagem_boas_vindas = f"{saudacao}, {nome_usuario} 😊, tudo bem?\n\n"

    # Envia a mensagem de boas-vindas com o nome do usuário, a saudação e os botões de opção
    with open(r"C:\Users\guuha\Documents\TG-Cardapio\Online\img\logo.png", "rb") as foto:
        bot.send_photo(chat_id, foto, caption=mensagem_boas_vindas, reply_markup=markup, parse_mode='Markdown')

# Manipulador de mensagens
@bot.message_handler(func=lambda message: True)
def manipular_mensagem(message):
    # Verifica se a mensagem foi enviada em um chat privado
    if message.chat.type == 'private':
        hora_atual = datetime.now().time()
        horario_inicial = datetime.strptime('11:00:00', '%H:%M:%S').time()
        horario_final = datetime.strptime('23:59:00', '%H:%M:%S').time()
        
        if horario_inicial <= hora_atual < horario_final:
            if message.chat.id not in dados_usuario:
                dados_usuario[message.chat.id] = {}
            dados_usuario[message.chat.id]['ultima_interacao'] = datetime.now()
            nome_usuario = message.from_user.first_name
            saudacao = obter_saudacao(hora_atual.hour)
            enviar_mensagem_boas_vindas(message.chat.id, nome_usuario, saudacao)
        else:
            mensagem = "Desculpe, o restaurante não está disponível fora do horário comercial *(das 11h00 às 24h)*. "
            mensagem += "Por favor, entre em contato novamente durante o horário de expediente. ⏰🔒"
            bot.send_message(message.chat.id, mensagem, parse_mode='Markdown')

# Manipulador de callback queries
@bot.callback_query_handler(func=lambda call: call.data in ['pagamento', 'voltarCardapio', 'chamarGarçom', 'cancelarPedido'])
def manipular_query_opcoes_iniciais(call):
    if call.data == 'pagamento':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='Débito', callback_data='debito')
        btn2 = types.InlineKeyboardButton(text='Crédito', callback_data='credito')
        btn3 = types.InlineKeyboardButton(text='Pix', callback_data='pix')
        markup.add(btn1, btn2, btn3)
        bot.send_message(call.message.chat.id, "Escolha a forma de pagamento:", reply_markup=markup)

    elif call.data == 'voltarCardapio':
        url = "https://tg-cardapio.vercel.app/"
        mensagem = f"Para voltar ao cardápio, clique no link abaixo:\n[Voltar ao Cardápio]({url})"
        bot.send_message(call.message.chat.id, mensagem, parse_mode='Markdown')

    elif call.data == 'chamarGarçom':
        bot.send_message(call.message.chat.id, "O garçom está a caminho! 🍽️")
    
    elif call.data == 'cancelarPedido':  # Nova condição
        bot.send_message(call.message.chat.id, "Seu pedido foi cancelado. Obrigado por visitar o nosso restaurante. 🍽️")
        bot.leave_chat(call.message.chat.id)  # Comando para o bot sair da conversa


# Função para gerar chave Pix
def gerar_chave_pix():
    chave_pix = str(uuid.uuid4())  # Gera uma chave Pix aleatória
    return chave_pix

# Função para gerar QR Code
def gerar_qrcode_pix(chave_pix):
    qr_data = f"pix:{chave_pix}"  # Informação para o QR Code (simples exemplo)
    img = qrcode.make(qr_data)  # Gera o QR Code com a chave Pix
    buf = io.BytesIO()  # Cria um buffer de memória
    img.save(buf, format='PNG')  # Salva o QR Code no buffer em formato PNG
    buf.seek(0)  # Move o cursor para o início do buffer
    return buf

# Manipulador para as opções de pagamento
@bot.callback_query_handler(func=lambda call: call.data in ['debito', 'credito', 'pix'])
def manipular_pagamento(call):
    if call.data == 'debito':
        bot.send_message(call.message.chat.id, "Você escolheu pagar com *Débito*.", parse_mode='Markdown')
    elif call.data == 'credito':
        bot.send_message(call.message.chat.id, "Você escolheu pagar com *Crédito*.", parse_mode='Markdown')
    elif call.data == 'pix':
        chave_pix = gerar_chave_pix()  # Gera a chave Pix
        qr_code = gerar_qrcode_pix(chave_pix)  # Gera o QR Code

        # Envia a chave Pix
        bot.send_message(call.message.chat.id, f"Sua chave Pix é: `{chave_pix}`", parse_mode='Markdown')

        # Envia o QR Code como imagem
        bot.send_photo(call.message.chat.id, qr_code, caption="Escaneie o QR Code para realizar o pagamento via Pix.")

# Inicia o polling do bot
bot.polling()
