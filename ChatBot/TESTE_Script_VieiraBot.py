import telebot
from telebot import types
from datetime import datetime

TOKEN_BOT = "7061009048:AAFqeIht-XctkKinw_CgfOQKHynPsC74iHs"

bot = telebot.TeleBot(TOKEN_BOT)

# Dicionário para armazenar os dados do usuário durante a conversa
user_data = {}
# Função para manipular mensagens recebidas
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Verifica se a mensagem foi enviada em um chat privado
    if message.chat.type == 'private':
        # Verifica se está dentro do horário comercial (8:30 às 18:00)
        current_time = datetime.now().time()
        start_time = datetime.strptime('08:30', '%H:%M').time()
        end_time = datetime.strptime('18:00', '%H:%M').time()
        
        if start_time <= current_time <= end_time:
            # Adiciona uma entrada para o ID do chat se ainda não existir
            if message.chat.id not in user_data:
                user_data[message.chat.id] = {}
            # Atualiza o timestamp da última mensagem recebida
            user_data[message.chat.id]['last_interaction'] = datetime.now()
            # Obtém o nome do usuário
            user_name = message.from_user.first_name
            # Determina a saudação com base na hora
            greeting = get_greeting(current_time.hour)
            # Envia a mensagem de boas-vindas com o nome do usuário e a saudação
            enviar_mensagem_boas_vindas(message.chat.id, user_name, greeting)
        else:
            # Fora do horário comercial, envia uma mensagem de aviso
            user_name = message.from_user.first_name
            bot.send_message(message.chat.id, f"Olá, {user_name}! 😊\n\nDesculpe, mas nosso suporte está disponível apenas durante o horário comercial, das **8:30 às 18:00**. Por favor, entre em contato conosco durante esse período. Obrigado!", parse_mode='Markdown')
# Função para determinar a saudação com base na hora
def get_greeting(hour):
    if 8 <= hour < 12:
        return "Bom dia"
    elif 12 <= hour < 19:
        return "Boa tarde"
    else:
        return "Olá"  
# Função para enviar mensagem de boas-vindas
def enviar_mensagem_boas_vindas(chat_id, user_name, greeting):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Suporte', callback_data='suporte')
    btn2 = types.InlineKeyboardButton(text='Logins', callback_data='logins')
    btn3 = types.InlineKeyboardButton(text='Dúvidas', callback_data='duvidas')
    btn4 = types.InlineKeyboardButton(text='Boas Práticas', callback_data='boas_praticas')
    markup.add(btn1, btn2, btn3, btn4)
    
    # Mensagem de boas-vindas
    welcome_message = f"{greeting}, {user_name} 😊, tudo bem?\n\n"
    welcome_message += "Aproveitando que você está aqui, já possui o software *AnyDesk* na sua máquina? Se não tiver, *clique no link abaixo para baixar*, ele é essencial para que eu consiga acessar seu computador se for necessário!\n\n"
    welcome_message += "[Baixar AnyDesk](https://download.anydesk.com/AnyDesk.exe)\n\n"
    welcome_message += "Agora que tem o software necessário, me diga como eu posso te ajudar? Para facilitar, *basta clicar nos botões abaixo!* ⬇️\n"

    # Envia a mensagem de boas-vindas com o nome do usuário, a saudação, a mensagem de sugestões e a imagem
    with open(r"C:\Users\mathe\Downloads\VieiraBot\wallpaper_vieiraCred.jpg", "rb") as photo:
        bot.send_photo(chat_id, photo, caption=welcome_message, reply_markup=markup, parse_mode='Markdown')
# Handler para seleção de opções iniciais
@bot.callback_query_handler(func=lambda call: call.data in ['suporte', 'logins', 'duvidas', 'boas_praticas'])
def callback_query_opcoes_iniciais(call):
    if call.data == 'suporte':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='Problema Resolvido', callback_data='problema_resolvido')
        btn2 = types.InlineKeyboardButton(text='Problema Persistiu', callback_data='problema_persistiu')
        markup.add(btn1, btn2)
        
        # Mensagem de boas-vindas
        resolve_message = "Antes de entrar em contato, vamos tentar resolver o problema juntos! 😊\n"
        resolve_message += "<b>Aqui estão algumas soluções rápidas que podem ajudar:</b>\n\n"
        resolve_message += "<b> • 🌎 Verifique se você está conectado à internet.</b>\n\n"
        resolve_message += "<b> • 🔌 Confirme se os cabos estão conectados corretamente.</b>\n\n"
        resolve_message += "<b> • 🔄 Reinicie o dispositivo ou o programa que está apresentando o problema.</b>\n\n"
        resolve_message += "<b> • ⚙️ Verifique se as configurações do dispositivo estão corretas (data, hora, som ligado...).</b>\n\n"
        resolve_message += "<b> • 🖱️ Se o problema for em algum acessório (Mouse, Teclado, Head). Tente trocar a porta onde ta conectado</b>\n\n\n"
        resolve_message += "Se nenhuma dessas soluções funcionar, não hesite em entrar em contato conosco para obter suporte especializado. 🛠️"
        
        bot.send_message(call.message.chat.id, resolve_message, reply_markup=markup, parse_mode='HTML')
    elif call.data == 'logins':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Argus', callback_data='argus_login')
        btn2 = types.InlineKeyboardButton(text='Ecorban', callback_data='ecorban_login')
        btn3 = types.InlineKeyboardButton(text='Servidor', callback_data='servidor_login')
        btn4 = types.InlineKeyboardButton(text='Email', callback_data='email')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(call.message.chat.id, "<b>Escolha uma das opções de login:</b>", reply_markup=markup, parse_mode='HTML')
        pass
    elif call.data == 'duvidas':
        bot.send_message(call.message.chat.id, "<b>Por favor, escreva sua dúvida:</b>", parse_mode='HTML')
        bot.register_next_step_handler(call.message, get_doubt)
        pass
    elif call.data == 'boas_praticas':
        texto = "🕘 <b>Horário de atendimento:</b>\n    • (Seg. Sex):   9hs-12hs | 13hs-18hs\n    • (Sábados):  9hs-12hs informar antes se vão trabalhar através de enquete\n\n📜 <b>Leia o Regulamento:</b>\n\n   👥 <b>Assuntos similares:</b> Os usuários poderão interagir e tratar de dúvidas e sugestões de Informática e Tecnologia sobre o helpdesk. Porém, só exija suporte conforme a Boas práticas de como solicitar suporte, pois o suporte é apenas para a ferramenta de utilidade da empresa e seus colaboradores.\n\n    🚦 <b>Por favor, evite fazer perguntas amadoras.</b> Peço encarecidamente a vocês que otimizem os chamados, tenha em mente que para trabalhar na área de informática ou qualquer outra, deve-se ter um conhecimento prévio.\n\n   🚨 <b>Favor não desobedecer as regras para não passar pelo inconveniente de ser advertido (perde a vez do seu atendimento) do grupo!</b> 🤝\n\n\n📝 <b>Boas práticas de como solicitar suporte:</b>\n   ➔ Explique o que deseja;\n   ➔ Nome do Operador da Máquina;\n   ➔ Nome da equipe do mesmo;\n   ➔ Mostre como está tentando fazer;\n   ➔ Informe detalhes da mensagem de erro e qual resultado diferente do esperado você está tendo.\n\n   <b>EXEMPLO:</b> Cole e Copie e preencha com o seu chamado 👍🏾\n    ➔ <b>PROBLEMA:</b> Meu Head não Funciona\n    ➔ <b>OPERADOR:</b> João\n    ➔ <b>EQUIPE:</b> Equipe João\n    ➔ <b>ACESSO ANYDESK:</b> 000000000\n\n📝 <b>Escreva a sua dificuldade ou dúvida.</b>\n\n⚠️ <b>OBS:</b> Devido a demanda de atendimentos, pode ser que não consigamos te atender de imediato ok.\nMas, não se preocupe, só aguardar a sua vez, que assim que puder a gente responde! ☺️👊"
        bot.send_message(call.message.chat.id, texto, parse_mode='HTML')
        pass

   
   
   
   
   
   
        
# SESSÃO [ SUPORTE ]
# Handler para a seleção de resolução de problemas do suporte
@bot.callback_query_handler(func=lambda call: call.data in ['problema_resolvido', 'problema_persistiu'])
def callback_query_problema_suporte(call):
    if call.data == 'problema_resolvido':
        bot.send_message(call.message.chat.id, "Fico feliz que o problema foi resolvido. Se precisar de mais alguma coisa basta entrar em contato conosco!")
    elif call.data == 'problema_persistiu':
        bot.send_message(call.message.chat.id, "Lamento que nada tenha funcionado, mas fique tranquilo que vamos resolver.\nPara isso, preencha as informações abaixo:")
        # Inicia o processo de coleta de informações para o problema
        iniciar_coleta_problema(call.message.chat.id)
# Função para iniciar o processo de coleta de informações para o problema
def iniciar_coleta_problema(chat_id):
    bot.send_message(chat_id, "Por favor, descreva qual é o problema que você está enfrentando:")
    bot.register_next_step_handler_by_chat_id(chat_id, get_problem)
# Função para obter o problema
def get_problem(message):
    user_data[message.chat.id]['problem'] = message.text
    bot.send_message(message.chat.id, f"Ótimo! O problema é: {message.text}")
    bot.send_message(message.chat.id, "Quem é o operador?")
    bot.register_next_step_handler(message, get_operator)
# Função para obter o operador
def get_operator(message):
    user_data[message.chat.id]['operator'] = message.text
    bot.send_message(message.chat.id, f"Entendi! O operador é: {message.text}")
    bot.send_message(message.chat.id, "Qual a equipe?")
    bot.register_next_step_handler(message, get_team)
# Função para obter a equipe
def get_team(message):
    user_data[message.chat.id]['team'] = message.text
    bot.send_message(message.chat.id, f"Certo! A equipe é: {message.text}")
    bot.send_message(message.chat.id, "Qual código AnyDesk?")
    bot.register_next_step_handler(message, get_anydesk)
# Função para obter o código AnyDesk
def get_anydesk(message):
    user_data[message.chat.id]['anydesk'] = message.text
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_confirmar = types.InlineKeyboardButton(text='Confirmar', callback_data='confirmar')
    btn_cancelar = types.InlineKeyboardButton(text='Cancelar', callback_data='cancelar')
    markup.add(btn_confirmar, btn_cancelar)
    bot.send_message(message.chat.id, f"Entendi! O código AnyDesk é: {message.text}\n\nPor favor, confirme as informações:", reply_markup=markup)
# Função para confirmar as informações
def confirm_information(message, confirmation_message):
    if confirmation_message == 'CONFIRMAR':
        enviar_mensagem_chats(["-1002108949408"], f"SUPORTE:\nEnviado por: {message.chat.username}\n\nPROBLEMA ➔ {user_data[message.chat.id]['problem']}\nOPERADOR ➔ {user_data[message.chat.id]['operator']}\nEQUIPE (Supervisor) ➔ {user_data[message.chat.id]['team']}\nANYDESK ➔ {user_data[message.chat.id]['anydesk']}", message.chat.id)
        mensagem_confirmacao = (
            "Suporte registrado!\n\n"
            "⚠️ <i>Por conta da demanda a resolução pode levar um tempo. "
            "Mas já estamos trabalhando para solucionar o seu problema</i>"
        )
        bot.send_message(message.chat.id, mensagem_confirmacao, parse_mode='HTML')
        # Limpa os dados da conversa desse usuário após o suporte ser registrado
        user_data.pop(message.chat.id, None)
    elif confirmation_message == 'CANCELAR':
        bot.send_message(message.chat.id, "Registro de suporte cancelado. Obrigado!")
        # Limpa os dados da conversa desse usuário após o cancelamento
        user_data.pop(message.chat.id, None)








# SESSÃO [ DÚVIDAS ]
# Função para obter a dúvida do usuário
def get_doubt(message):
    user_data[message.chat.id]['doubt'] = message.text
    bot.send_message(message.chat.id, "Obrigado por sua pergunta! Nós entraremos em contato em breve.")
    enviar_mensagem_chats(["-1002108949408"], f"DUVIDA: \nDúvida de {message.chat.username}\n\nDúvida ➔ '{message.text}'", message.chat.id)








# SESSÃO [ LOGIN ]
# Handlers para as opções de login
@bot.callback_query_handler(func=lambda call: call.data in ['argus_login', 'ecorban_login', 'servidor_login', 'email'])
def callback_query_login_options(call):
    if call.data == 'argus_login':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_resetar = types.InlineKeyboardButton(text='Resetar', callback_data='argus_resetar')
        btn_cancelar = types.InlineKeyboardButton(text='Cancelar', callback_data='argus_cancelar')
        markup.add(btn_resetar, btn_cancelar)
        msgInfoArgus = "No momento a equipe de T.I. faz apenas o <b>reset da senha</b>.\nCaso precise de algo além, clique em <b>'cancelar'</b> e\nprocure o <b>Financeiro!</b>"
        bot.send_message(call.message.chat.id, msgInfoArgus, reply_markup=markup, parse_mode='HTML')
    elif call.data == 'ecorban_login':
        bot.send_message(call.message.chat.id, "Okay, para resolver seu problema preciso que me envie algumas informações.")
        bot.send_message(call.message.chat.id, "Qual o problema?")
        bot.register_next_step_handler(call.message, get_ecorban_info)
    elif call.data == 'servidor_login':
        bot.send_message(call.message.chat.id, "Okay, para resolver seu problema preciso que me envie algumas informações.")
        bot.send_message(call.message.chat.id, "Por favor, envie o nome completo do usuário:")
        bot.register_next_step_handler(call.message, get_servidor_info)
    elif call.data == 'email':
        solicitar_informacoes_email(call.message.chat.id)








# SESSÃO [ ARGUS ]
# Handlers para as opções de reset de senha do Argus
@bot.callback_query_handler(func=lambda call: call.data in ['argus_resetar', 'argus_cancelar'])
def callback_query_argus_resetar(call):
    if call.data == 'argus_resetar':
        bot.send_message(call.message.chat.id, "Por favor, envie o nome do usuário para o qual deseja resetar a senha:")
        bot.register_next_step_handler(call.message, resetar_senha_argus)
    elif call.data == 'argus_cancelar':
        bot.send_message(call.message.chat.id, "Agradecemos o seu contato. Se precisar de mais alguma coisa, não hesite em nos chamar!")
# Função para obter o nome de usuário do Argus
def get_argus_username(message):
    user_data[message.chat.id]['argus_username'] = message.text
    bot.send_message(message.chat.id, "Obrigado! \nJa estamos trabalhando para resolver seu problema. Assim que finalizar-mos, entraremos em contato para confirmar.")
    # Aqui você pode adicionar a lógica para processar o reset da senha do Argus com o nome de usuário fornecido
# Handler para as opções de reset de senha do Argus
@bot.callback_query_handler(func=lambda call: call.data in ['argus_resetar', 'argus_cancelar'])
def callback_query_argus_options(call):
    if call.data == 'argus_resetar':
        bot.send_message(call.message.chat.id, "Por favor, envie o nome do usuário para o qual deseja resetar a senha.")
        bot.register_next_step_handler(call.message, get_argus_username)
    elif call.data == 'argus_cancelar':
        bot.send_message(call.message.chat.id, "Agradecemos o seu contato. Se precisar de mais alguma coisa, não hesite em nos chamar!")
# Função para resetar a senha do Argus
def resetar_senha_argus(message):
    username = message.text
    bot.send_message(message.chat.id, f"Você solicitou o reset da senha para o usuário: {username}. \nJa estamos trabalhando para resolver seu problema. Assim que finalizar-mos, entraremos em contato para confirmar.")
    enviar_mensagem_chats(["-1002108949408"], f"ARGUS:\nEnviado por: {message.chat.username}\n\nNome completo ➔ {username}", message.chat.id)








# SESSÃO [ ECORBAN ]
# Função para obter as informações do usuário Ecorban
def get_ecorban_info(message):
    # Armazena o problema relatado pelo usuário
    user_data[message.chat.id]['ecorban_problem'] = message.text
    # Solicita o nome do usuário
    bot.send_message(message.chat.id, "Nome do usuário:")
    bot.register_next_step_handler(message, get_ecorban_username)
# Função para obter o nome do usuário Ecorban
def get_ecorban_username(message):
    # Armazena o nome do usuário
    user_data[message.chat.id]['ecorban_username'] = message.text
    # Solicita a empresa do usuário
    bot.send_message(message.chat.id, "Empresa do usuário:")
    bot.register_next_step_handler(message, get_ecorban_company)
# Função para obter a empresa do usuário Ecorban
def get_ecorban_company(message):
    # Armazena a empresa do usuário
    user_data[message.chat.id]['ecorban_company'] = message.text
    # Solicita o cargo do usuário
    bot.send_message(message.chat.id, "Cargo do usuário:")
    bot.register_next_step_handler(message, get_ecorban_position)
# Função para obter o cargo do usuário Ecorban
def get_ecorban_position(message):
    # Armazena o cargo do usuário
    user_data[message.chat.id]['ecorban_position'] = message.text
    # Solicita o CPF do usuário
    bot.send_message(message.chat.id, "CPF do usuário:")
    bot.register_next_step_handler(message, get_ecorban_cpf)
# Função para obter o CPF do usuário Ecorban
def get_ecorban_cpf(message):
    # Armazena o CPF do usuário
    user_data[message.chat.id]['ecorban_cpf'] = message.text
    # Solicita informações adicionais, se houver
    bot.send_message(message.chat.id, "Alguma informação adicional?")
    bot.register_next_step_handler(message, confirm_ecorban_info)
# Função para confirmar as informações do usuário Ecorban
def confirm_ecorban_info(message):
    # Cria uma mensagem com todas as informações coletadas
    ecorban_info = (
        "ECORBAN:\n"
        f"Enviado por: {message.chat.username}\n\n"
        f"Problema ➔ {user_data[message.chat.id]['ecorban_problem']}\n"
        f"Nome do usuário ➔ {user_data[message.chat.id]['ecorban_username']}\n"
        f"Empresa do usuário ➔ {user_data[message.chat.id]['ecorban_company']}\n"
        f"Cargo do usuário ➔ {user_data[message.chat.id]['ecorban_position']}\n"
        f"CPF do usuário ➔ {user_data[message.chat.id]['ecorban_cpf']}\n"
        f"Informação adicional ➔ {message.text}"
    )

    # Cria botões para confirmar ou cancelar as informações
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_confirmar = types.InlineKeyboardButton(text='Confirmar', callback_data='ecorban_confirmar')
    btn_cancelar = types.InlineKeyboardButton(text='Cancelar', callback_data='ecorban_cancelar')
    markup.add(btn_confirmar, btn_cancelar)

    # Envia a mensagem com as informações e os botões para confirmação
    bot.send_message(message.chat.id, "Por favor, confirme as informações:", reply_markup=markup)
    # Armazena as informações para possível uso posterior
    user_data[message.chat.id]['ecorban_info'] = ecorban_info
# Handlers para a confirmação das informações Ecorban
@bot.callback_query_handler(func=lambda call: call.data in ['ecorban_confirmar', 'ecorban_cancelar'])
def callback_query_ecorban_confirmation(call):
    if call.data == 'ecorban_confirmar':
        # Envia as informações confirmadas para um grupo específico ou canal
        enviar_mensagem_chats(["-1002108949408"], user_data[call.message.chat.id]['ecorban_info'], call.message.chat.id)
        bot.send_message(call.message.chat.id, "Agradecemos o seu contato. \nJa estamos trabalhando para resolver seu problema. Assim que finalizarmos, entraremos em contato para confirmar.")
    elif call.data == 'ecorban_cancelar':
        bot.send_message(call.message.chat.id, "Agradecemos o seu contato. Se precisar de mais alguma coisa, não hesite em nos chamar!")





  
  
     
# SESSÃO [ SERVIDOR ]
# Handlers para a confirmação das informações do servidor
@bot.callback_query_handler(func=lambda call: call.data in ['servidor_confirmar', 'servidor_cancelar'])
def callback_query_servidor_confirmation(call):
    if call.data == 'servidor_confirmar':
        servidor_username = user_data[call.message.chat.id]['servidor_username']
        servidor_problem = user_data[call.message.chat.id]['servidor_problem']
        enviar_mensagem_chats(["-1002108949408"], f"SERVIDOR\nEnviado por: {call.message.chat.username}\n\n Nome completo do usuário ➔ {servidor_username}\nProblema ➔ {servidor_problem}", call.message.chat.id)
        bot.send_message(call.message.chat.id, "Agradecemos o seu contato. \nJa estamos trabalhando para resolver seu problema. Assim que finalizar-mos, entraremos em contato para confirmar.")
        bot.send_message(call.message.chat.id, "Agradecemos o seu contato. Se precisar de mais alguma coisa, não hesite em nos chamar!")
# Função para obter informações do usuário para a opção "Argus"
def get_servidor_info(message):
    user_data[message.chat.id]['servidor_username'] = message.text
    bot.send_message(message.chat.id, "Agora, descreva o problema:")
    bot.register_next_step_handler(message, get_servidor_problem)
# Função para obter o problema do usuário para a opção "Argus"
def get_servidor_problem(message):
    user_data[message.chat.id]['servidor_problem'] = message.text
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_confirmar = types.InlineKeyboardButton(text='Confirmar', callback_data='servidor_confirmar')
    btn_cancelar = types.InlineKeyboardButton(text='Cancelar', callback_data='servidor_cancelar')
    markup.add(btn_confirmar, btn_cancelar)
    bot.send_message(message.chat.id, "Por favor, confirme se as informações estão corretas:", reply_markup=markup)







 
# SESSÃO [ EMAIL ]
# Função para solicitar informações de email
def solicitar_informacoes_email(chat_id):
    bot.send_message(chat_id, "Por favor, insira seu nome completo:")
    bot.register_next_step_handler_by_chat_id(chat_id, get_nome_completo)
# Função para obter nome completo
def get_nome_completo(message):
    user_data[message.chat.id]['nome_completo'] = message.text
    bot.send_message(message.chat.id, "Agora, por favor, insira seu cargo:")
    bot.register_next_step_handler(message, get_cargo)
# Função para obter cargo
def get_cargo(message):
    user_data[message.chat.id]['cargo'] = message.text
    enviar_mensagem_confirmacao_email(message.chat.id)
# Função para enviar mensagem de confirmação de email
def enviar_mensagem_confirmacao_email(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_confirmar = types.InlineKeyboardButton(text='Confirmar', callback_data='confirmar_email')
    btn_cancelar = types.InlineKeyboardButton(text='Cancelar', callback_data='cancelar_email')
    markup.add(btn_confirmar, btn_cancelar)
    bot.send_message(chat_id, "As informações fornecidas estão corretas?", reply_markup=markup)
# Handlers para confirmação de email
@bot.callback_query_handler(func=lambda call: call.data in ['confirmar_email', 'cancelar_email'])
def callback_query_confirmar_email(call):
    if call.data == 'confirmar_email':
        # Nome completo do usuário
        nome_completo = user_data[call.message.chat.id]['nome_completo']
        
        # Cargo enviado
        cargo = user_data[call.message.chat.id]['cargo']
        
        # Envie mensagem de agradecimento e pedido de aguardar
        bot.send_message(call.message.chat.id, "Obrigado! Por favor, aguarde enquanto processamos suas informações.")
        
        # Envie mensagem de confirmação para chat específico
        enviar_mensagem_chats(["-1002108949408"], f"EMAIL:\nEnviado por: {call.message.chat.username}\n\nNome completo ➔ {nome_completo}\nCargo ➔ {cargo}", call.message.chat.id)
    elif call.data == 'cancelar_email':
        # Envie mensagem de cancelamento
        bot.send_message(call.message.chat.id, "Solicitação de email cancelada. Obrigado!")








# SESSÃO [ FUNÇÕES A PARTE ]
# Função para enviar mensagem para os chats específicos, excluindo o chat_id do usuário
def enviar_mensagem_chats(chat_ids, message, user_chat_id):
    for chat_id in chat_ids:
        if str(chat_id) != str(user_chat_id):
            bot.send_message(chat_id, message)
# Função para manipular mensagens recebidas
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    enviar_mensagem_boas_vindas(message.chat.id)

bot.polling()
