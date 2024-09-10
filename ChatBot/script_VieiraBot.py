import telebot # type: ignore
from telebot import types # type: ignore
from datetime import datetime

# Token do seu bot
TOKEN_BOT = "7061009048:AAFqeIht-XctkKinw_CgfOQKHynPsC74iHs"

# Dicionário para armazenar os dados do usuário durante a conversa
dados_usuario = {}

# Dicionário para armazenar informações do usuário durante o suporte do Ecorban
dados_usuario_ecorban = {}

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
        return "Olá"

# Função para enviar mensagem de boas-vindas
def enviar_mensagem_boas_vindas(chat_id, nome_usuario, saudacao):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Suporte', callback_data='suporte')
    btn2 = types.InlineKeyboardButton(text='Logins', callback_data='logins')
    btn3 = types.InlineKeyboardButton(text='Dúvidas', callback_data='duvidas')
    btn4 = types.InlineKeyboardButton(text='Boas Práticas', callback_data='boas_praticas')
    markup.add(btn1, btn2, btn3, btn4)
    
    # Mensagem de boas-vindas
    mensagem_boas_vindas = f"{saudacao}, {nome_usuario} 😊, tudo bem?\n\n"
    mensagem_boas_vindas += "Aproveitando que você está aqui, já possui o software *AnyDesk* na sua máquina? Se não tiver, *clique no link abaixo para baixar*, ele é essencial para que eu consiga acessar seu computador se for necessário!\n\n"
    mensagem_boas_vindas += "[Baixar AnyDesk](https://download.anydesk.com/AnyDesk.exe)\n\n"
    mensagem_boas_vindas += "Agora que tem o software necessário, me diga como eu posso te ajudar? Para facilitar, *basta clicar nos botões abaixo!* ⬇️\n"

    # Envia a mensagem de boas-vindas com o nome do usuário, a saudação e os botões de opção
    with open(r"C:\Users\mathe\Downloads\VieiraBot\wallpaper_vieiraCred.jpg", "rb") as foto:
        bot.send_photo(chat_id, foto, caption=mensagem_boas_vindas, reply_markup=markup, parse_mode='Markdown')

# Manipulador de mensagens
@bot.message_handler(func=lambda message: True)
def manipular_mensagem(message):
    # Verifica se a mensagem foi enviada em um chat privado
    if message.chat.type == 'private':
        # Verifica se está dentro do horário comercial (das 8h30 às 18h)
        hora_atual = datetime.now().time()
        horario_inicial = datetime.strptime('08:30:00', '%H:%M:%S').time()
        horario_final = datetime.strptime('18:00:00', '%H:%M:%S').time()
        
        if horario_inicial <= hora_atual < horario_final:
            # Adiciona uma entrada para o ID do chat se ainda não existir
            if message.chat.id not in dados_usuario:
                dados_usuario[message.chat.id] = {}
            # Atualiza o timestamp da última interação
            dados_usuario[message.chat.id]['ultima_interacao'] = datetime.now()
            # Obtém o nome do usuário
            nome_usuario = message.from_user.first_name
            # Determina a saudação com base na hora
            saudacao = obter_saudacao(hora_atual.hour)
            # Envia a mensagem de boas-vindas
            enviar_mensagem_boas_vindas(message.chat.id, nome_usuario, saudacao)
        else:
            # Fora do horário comercial, envia uma mensagem informando que o suporte não está disponível
            mensagem = "Desculpe, o suporte não está disponível fora do horário comercial *(das 8h30 às 18h)*. "
            mensagem += "Por favor, entre em contato novamente durante o horário de expediente. ⏰🔒"
            bot.send_message(message.chat.id, mensagem, parse_mode='Markdown')

# Manipulador para seleção de opções iniciais
@bot.callback_query_handler(func=lambda call: call.data in ['suporte', 'logins', 'duvidas', 'boas_praticas'])
def manipular_query_opcoes_iniciais(call):
    if call.data == 'suporte':
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='Problema Resolvido', callback_data='problema_resolvido')
        btn2 = types.InlineKeyboardButton(text='Problema Persistiu', callback_data='problema_persistiu')
        markup.add(btn1, btn2)
        
        # Mensagem com soluções rápidas
        mensagem_solucoes = "Antes de entrar em contato, vamos tentar resolver o problema juntos! 😊\n"
        mensagem_solucoes += "<b>Aqui estão algumas soluções rápidas que podem ajudar:</b>\n\n"
        mensagem_solucoes += "<b> • 🌎 Verifique se você está conectado à internet.</b>\n\n"
        mensagem_solucoes += "<b> • 🔌 Confirme se os cabos estão conectados corretamente.</b>\n\n"
        mensagem_solucoes += "<b> • 🔄 Reinicie o dispositivo ou o programa que está apresentando o problema.</b>\n\n"
        mensagem_solucoes += "<b> • ⚙️ Verifique se as configurações do dispositivo estão corretas (data, hora, som ligado...).</b>\n\n"
        mensagem_solucoes += "<b> • 🖱️ Se o problema for em algum acessório (Mouse, Teclado, Head). Tente trocar a porta onde ta conectado</b>\n\n\n"
        mensagem_solucoes += "Se nenhuma dessas soluções funcionar, não hesite em entrar em contato conosco para obter suporte especializado. 🛠️"
        
        bot.send_message(call.message.chat.id, mensagem_solucoes, reply_markup=markup, parse_mode='HTML')
    elif call.data == 'logins':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Argus', callback_data='argus_login')
        btn2 = types.InlineKeyboardButton(text='Ecorban', callback_data='ecorban_login')
        btn3 = types.InlineKeyboardButton(text='Servidor', callback_data='servidor_login')
        btn4 = types.InlineKeyboardButton(text='Email', callback_data='email')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(call.message.chat.id, "<b>Escolha uma das opções de login:</b>", reply_markup=markup, parse_mode='HTML')
    elif call.data == 'duvidas':
        bot.send_message(call.message.chat.id, "<b>Por favor, escreva sua dúvida:</b>", parse_mode='HTML')
        bot.register_next_step_handler(call.message, obter_duvida)
    elif call.data == 'boas_praticas':
        mensagem_boas_praticas = "🕘 <b>Horário de atendimento:</b>\n    • (Seg. Sex):   9hs-12hs | 13hs-18hs\n    • (Sábados):  9hs-12hs informar antes se vão trabalhar através de enquete\n\n📜 <b>Leia o Regulamento:</b>\n\n   👥 <b>Assuntos similares:</b> Os usuários poderão interagir e tratar de dúvidas e sugestões de Informática e Tecnologia sobre o helpdesk. Porém, só exija suporte conforme a Boas práticas de como solicitar suporte, pois o suporte é apenas para a ferramenta de utilidade da empresa e seus colaboradores.\n\n    🚦 <b>Por favor, evite fazer perguntas amadoras.</b> Peço encarecidamente a vocês que otimizem os chamados, tenha em mente que para trabalhar na área de informática ou qualquer outra, deve-se ter um conhecimento prévio.\n\n   🚨 <b>Favor não desobedecer as regras para não passar pelo inconveniente de ser advertido (perde a vez do seu atendimento) do grupo!</b> 🤝\n\n\n📝 <b>Boas práticas de como solicitar suporte:</b>\n   ➔ Explique o que deseja;\n   ➔ Nome do Operador da Máquina;\n   ➔ Nome da equipe do mesmo;\n   ➔ Mostre como está tentando fazer;\n   ➔ Informe detalhes da mensagem de erro e qual resultado diferente do esperado você está tendo.\n\n   <b>EXEMPLO:</b> Cole e Copie e preencha com o seu chamado 👍🏾\n    ➔ <b>PROBLEMA:</b> Meu Head não Funciona\n    ➔ <b>OPERADOR:</b> João\n    ➔ <b>EQUIPE (Supervisor):</b> Equipe João\n    ➔ <b>ACESSO ANYDESK:</b> 000000000\n\n📝 <b>Escreva a sua dificuldade ou dúvida.</b>\n\n⚠️ <b>OBS:</b> Devido a demanda de atendimentos, pode ser que não consigamos te atender de imediato ok.\nMas, não se preocupe, só aguardar a sua vez, que assim que puder a gente responde! ☺️👊"
        bot.send_message(call.message.chat.id, mensagem_boas_praticas, parse_mode='HTML')




# SESSÃO DE [PRÉ-SUPORTE]

# Handler para a seleção de resolução de problemas do suporte
@bot.callback_query_handler(func=lambda call: call.data in ['problema_resolvido', 'problema_persistiu'])
def callback_query_problema_suporte(call):
    if call.data == 'problema_resolvido':
        # Envia mensagem de confirmação de resolução
        bot.send_message(call.message.chat.id, "Fico feliz que o problema foi resolvido. Se precisar de mais alguma coisa basta entrar em contato conosco!")
    elif call.data == 'problema_persistiu':
        # Envia mensagem de apoio e solicitação de informações adicionais
        bot.send_message(call.message.chat.id, "Lamento que nada tenha funcionado, mas fique tranquilo que vamos resolver.\nPara isso, preencha as informações abaixo:")
        # Inicia o processo de coleta de informações para o problema
        iniciar_coleta_problema(call.message.chat.id)





# SESSÃO DE [SUPORTE]

# Função para iniciar o processo de coleta de informações para o problema
def iniciar_coleta_problema(chat_id):
    template = (
        "Por favor, descreva qual é o problema que você está enfrentando utilizando o template (⚠️ É necessário copiar e colar todo o texto abaixo):\n\n"
        "PROBLEMA:\nOPERADOR:\nEQUIPE (Supervisor):\nACESSO ANYDESK:"
    )
    bot.send_message(chat_id, template, parse_mode='Markdown')
    bot.register_next_step_handler_by_chat_id(chat_id, obter_problema)
# Função para obter o problema e demais informações
def obter_problema(message):
    lines = message.text.split('\n')
    problem, operator, team, anydesk = '', '', '', ''
    for line in lines:
        if 'PROBLEMA:' in line:
            problem = line.replace('PROBLEMA:', '').strip()
        elif 'OPERADOR:' in line:
            operator = line.replace('OPERADOR:', '').strip()
        elif 'EQUIPE (Supervisor):' in line:
            team = line.replace('EQUIPE (Supervisor):', '').strip()
        elif 'ACESSO ANYDESK:' in line:
            anydesk = line.replace('ACESSO ANYDESK:', '').strip()
    
    # Verificar se pelo menos um campo foi preenchido
    if problem or operator or team or anydesk:
        # Se algum campo estiver preenchido, envie a mensagem de suporte
        support_message = (
            f"PROBLEMA ➔ {problem}\n"
            f"OPERADOR ➔ {operator}\n"
            f"EQUIPE (Supervisor) ➔ {team}\n"
            f"ANYDESK ➔ {anydesk}"
        )
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_confirmar = types.InlineKeyboardButton(text='Confirmar', callback_data='confirmar_mensagem')
        btn_cancelar = types.InlineKeyboardButton(text='Cancelar', callback_data='cancelar_mensagem')
        markup.add(btn_confirmar, btn_cancelar)
        bot.send_message(message.chat.id, f"Enviado por {message.chat.username}:\n\n{support_message}", reply_markup=markup)
        # Armazenar as informações no dicionário dados_usuario
        dados_usuario[message.chat.id] = {
            'problem': problem,
            'operator': operator,
            'team': team,
            'anydesk': anydesk
        }
    else:
        # Se nenhum campo estiver preenchido, solicite ao usuário que forneça informações
        bot.send_message(message.chat.id, "Por favor, forneça pelo menos uma informação.")
# Handler para os botões de confirmação e cancelamento
@bot.callback_query_handler(func=lambda call: call.data in ['confirmar_mensagem', 'cancelar_mensagem'])
def callback_query_confirmar_cancelar_mensagem(call):
    if call.data == 'confirmar_mensagem':
        enviar_informacoes_suporte(call.message, call.data)
        mensagem_confirmacao = (
            "Suporte registrado!\n\n"
            "⚠️ <i>Por conta da demanda a resolução pode levar um tempo. "
            "Mas já estamos trabalhando para solucionar o seu problema</i>"
        )
        bot.send_message(call.message.chat.id, mensagem_confirmacao, parse_mode='HTML')
    elif call.data == 'cancelar_mensagem':
        mensagem_cancelamento = "Atendimento de suporte cancelado com sucesso. Qualquer coisa estaremos à disposição!"
# Função para enviar as informações do suporte para todos os chats específicos
def enviar_informacoes_suporte(message, confirmation_message):
    if confirmation_message == 'confirmar_mensagem':
        support_message = (
            f"SUPORTE: {message.chat.username}\n\n"
            f"➔ PROBLEMA: {dados_usuario[message.chat.id]['problem']}\n"
            f"➔ OPERADOR: {dados_usuario[message.chat.id]['operator']}\n"
            f"➔ EQUIPE: {dados_usuario[message.chat.id]['team']}\n"
            f"➔ ACESSO ANYDESK: {dados_usuario[message.chat.id]['anydesk']}"
        )
        bot.send_message("-1002125287134", support_message)





# SESSÃO DE [DÚVIDAS]

# Função para obter a dúvida do usuário
def obter_duvida(message):
    # Armazena a dúvida do usuário nos dados do usuário
    dados_usuario[message.chat.id]['duvida'] = message.text
    # Envia uma mensagem de agradecimento ao usuário
    bot.send_message(message.chat.id, "Obrigado por sua pergunta! Nós entraremos em contato em breve.")
    # Envia a dúvida para o grupo responsável pelo suporte
    enviar_mensagem_chats(["-1002125287134"], f"DÚVIDA:\n\nDúvida de: {message.chat.username}\n\n'{message.text}'", message.chat.id)





# SESSÃO DE [LOGIN] 

# Handlers para as opções de login
@bot.callback_query_handler(func=lambda call: call.data in ['argus_login', 'ecorban_login', 'servidor_login', 'email'])
def callback_query_opcoes_login(call):
    if call.data == 'argus_login':
        # Criação dos botões para resetar ou cancelar
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_resetar = types.InlineKeyboardButton(text='Resetar', callback_data='argus_resetar')
        btn_cancelar = types.InlineKeyboardButton(text='Cancelar', callback_data='argus_cancelar')
        markup.add(btn_resetar, btn_cancelar)
        
        # Mensagem informativa para o login do Argus
        msg_info_argus = "No momento, a equipe de T.I. realiza apenas o <b>reset da senha</b>.\nCaso precise de algo além, clique em <b>'Cancelar'</b> e\nprocure o <b>Financeiro!</b>"
        
        # Envio da mensagem informativa
        bot.send_message(call.message.chat.id, msg_info_argus, reply_markup=markup, parse_mode='HTML')
    elif call.data == 'ecorban_login':
        # Solicita informações para resolver o problema do Ecorban
        bot.send_message(call.message.chat.id, "Para resolver seu problema, preciso que me envie algumas informações.")
        iniciar_coleta_problema_ecorban(call.message.chat.id)  # Passando apenas o chat_id
    elif call.data == 'servidor_login':
        # Solicita informações para resolver o problema do Servidor
        bot.send_message(call.message.chat.id, "Para resolver seu problema, preciso que me envie algumas informações.")
        bot.send_message(call.message.chat.id, "Por favor, envie o nome completo do usuário:")
        bot.register_next_step_handler(call.message, obter_informacoes_servidor)
    elif call.data == 'email':
        # Solicita informações para o email
        iniciar_coleta_email(call.message.chat.id)





# SESSÃO DE [ARGUS]:

# Handlers para as opções de reset de senha do Argus
@bot.callback_query_handler(func=lambda call: call.data in ['argus_resetar', 'argus_cancelar'])
def callback_query_opcoes_reset_senha_argus(call):
    if call.data == 'argus_resetar':
        bot.send_message(call.message.chat.id, "Por favor, envie o nome do usuário para o qual deseja resetar a senha:")
        bot.register_next_step_handler(call.message, resetar_senha_argus)
    elif call.data == 'argus_cancelar':
        bot.send_message(call.message.chat.id, "Agradecemos o seu contato. Se precisar de mais alguma coisa, não hesite em nos chamar!")
# Função para resetar a senha do Argus
def resetar_senha_argus(message):
    username = message.text
    bot.send_message(message.chat.id, f"Você solicitou o reset da senha para o usuário: {username}. \nJá estamos trabalhando para resolver seu problema. Assim que finalizarmos, entraremos em contato para confirmar.")
    enviar_mensagem_chats(["-1002125287134"], f"ARGUS:\nEnviado por: {message.chat.username}\n\nSolicitação de reset de senha para o usuário: {username}", message.chat.id)
# Função para obter o nome de usuário do Argus
def obter_nome_usuario_argus(message):
    dados_usuario[message.chat.id]['argus_username'] = message.text
    bot.send_message(message.chat.id, "Obrigado! \nJá estamos trabalhando para resolver seu problema. Assim que finalizarmos, entraremos em contato para confirmar.")
    # Aqui você pode adicionar a lógica para processar o reset da senha do Argus com o nome de usuário fornecido





# SESSÃO DE [ECORBAN]

# Função para iniciar o processo de coleta de informações para o problema do Ecorban
def iniciar_coleta_problema_ecorban(chat_id):
    template = (
        "Para resolver seu problema, preciso que me envie algumas informações.\n\n"
        "Por favor, descreva o que você precisa. "
        "Escreva da seguinte maneira para facilitar a solução  (⚠️ É necessário copiar e colar todo o texto abaixo):\n\n"
        "PROBLEMA:\nNOME COMPLETO DO USUÁRIO:\nEMPRESA DO USUÁRIO:\nCARGO DO USUÁRIO:\nCPF DO USUÁRIO:\nINFORMAÇÃO ADICIONAL:"
    )
    bot.send_message(chat_id, template, parse_mode='Markdown')
    bot.register_next_step_handler_by_chat_id(chat_id, obter_problema_ecorban)
# Função para obter o problema e demais informações do Ecorban
def obter_problema_ecorban(message):
    lines = message.text.split('\n')
    problem, user_fullname, user_company, user_position, user_cpf, additional_info = '', '', '', '', '', ''
    for line in lines:
        if 'PROBLEMA:' in line:
            problem = line.replace('PROBLEMA:', '').strip()
        elif 'NOME COMPLETO DO USUÁRIO:' in line:
            user_fullname = line.replace('NOME COMPLETO DO USUÁRIO:', '').strip()
        elif 'EMPRESA DO USUÁRIO:' in line:
            user_company = line.replace('EMPRESA DO USUÁRIO:', '').strip()
        elif 'CARGO DO USUÁRIO:' in line:
            user_position = line.replace('CARGO DO USUÁRIO:', '').strip()
        elif 'CPF DO USUÁRIO:' in line:
            user_cpf = line.replace('CPF DO USUÁRIO:', '').strip()
        elif 'INFORMAÇÃO ADICIONAL:' in line:
            additional_info = line.replace('INFORMAÇÃO ADICIONAL:', '').strip()
    
    if problem and user_fullname and user_company and user_position and user_cpf and additional_info:
        support_message = (
            f"PROBLEMA ➔ {problem}\n"
            f"NOME COMPLETO ➔ {user_fullname}\n"
            f"EMPRESA ➔ {user_company}\n"
            f"CARGO ➔ {user_position}\n"
            f"CPF ➔ {user_cpf}\n"
            f"INFORMAÇÃO ADICIONAL ➔ {additional_info}"
        )
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_confirmar = types.InlineKeyboardButton(text='Confirmar', callback_data='confirmar_mensagem_ecorban')
        btn_cancelar = types.InlineKeyboardButton(text='Cancelar', callback_data='cancelar_mensagem_ecorban')
        markup.add(btn_confirmar, btn_cancelar)
        bot.send_message(message.chat.id, f"Enviado por {message.chat.username}:\n\n{support_message}", reply_markup=markup)
        # Armazenar as informações no dicionário dados_usuario_ecorban
        dados_usuario_ecorban[message.chat.id] = {
            'problem': problem,
            'user_fullname': user_fullname,
            'user_company': user_company,
            'user_position': user_position,
            'user_cpf': user_cpf,
            'additional_info': additional_info
        }
    else:
        bot.send_message(message.chat.id, "Por favor, forneça todas as informações solicitadas.")
# Handler para os botões de confirmação e cancelamento para a sessão Ecorban
@bot.callback_query_handler(func=lambda call: call.data in ['confirmar_mensagem_ecorban', 'cancelar_mensagem_ecorban'])
def callback_query_confirmar_cancelar_mensagem_ecorban(call):
    if call.data == 'confirmar_mensagem_ecorban':
        enviar_informacoes_suporte_ecorban(call.message, call.data)
        mensagem_confirmacao = (
            "Sua solicitação foi registrada. Estamos trabalhando para resolver seu problema. "
            "Entraremos em contato assim que tivermos uma atualização."
        )
        bot.send_message(call.message.chat.id, mensagem_confirmacao)
    elif call.data == 'cancelar_mensagem_ecorban':
        mensagem_cancelamento = "Atendimento de suporte cancelado com sucesso. Se precisar de mais alguma coisa, estamos à disposição!"
# Função para enviar as informações do suporte para todos os chats específicos para a sessão Ecorban
def enviar_informacoes_suporte_ecorban(message, confirmation_message):
    if confirmation_message == 'confirmar_mensagem_ecorban':
        support_message = (
            f"ECORBAN: {message.chat.username}\n\n"
            f"➔ PROBLEMA: {dados_usuario_ecorban[message.chat.id]['problem']}\n"
            f"➔ NOME COMPLETO: {dados_usuario_ecorban[message.chat.id]['user_fullname']}\n"
            f"➔ EMPRESA: {dados_usuario_ecorban[message.chat.id]['user_company']}\n"
            f"➔ CARGO: {dados_usuario_ecorban[message.chat.id]['user_position']}\n"
            f"➔ CPF: {dados_usuario_ecorban[message.chat.id]['user_cpf']}\n"
            f"➔ INFORMAÇÃO ADICIONAL: {dados_usuario_ecorban[message.chat.id]['additional_info']}"
        )
        bot.send_message("-1002125287134", support_message)

    
    
    
    
# SESSÃO DE [SERVIDOR]
    
# Handlers para a confirmação das informações do servidor
@bot.callback_query_handler(func=lambda call: call.data in ['servidor_confirmar', 'servidor_cancelar'])
def callback_query_confirmacao_servidor(call):
    if call.data == 'servidor_confirmar':
        # Obtém as informações do usuário
        servidor_nome_completo = dados_usuario[call.message.chat.id]['servidor_nome_completo']
        servidor_problema = dados_usuario[call.message.chat.id]['servidor_problema']
        
        # Envia as informações para o grupo de suporte
        enviar_mensagem_chats(["-1002125287134"], f"SERVIDOR\nEnviado por: {call.message.chat.username}\n\n Nome completo do usuário: {servidor_nome_completo}\nProblema: {servidor_problema}", call.message.chat.id)
        
        # Mensagem de agradecimento e informação sobre o processo de resolução
        bot.send_message(call.message.chat.id, "Agradecemos o seu contato. Já estamos trabalhando para resolver seu problema. Assim que finalizarmos, entraremos em contato para confirmar.")
    elif call.data == 'servidor_cancelar':
        # Mensagem de agradecimento pelo contato e indicação para futuras necessidades
        bot.send_message(call.message.chat.id, "Agradecemos o seu contato. Se precisar de mais alguma coisa, não hesite em nos chamar!")
# Função para obter informações do usuário para a opção "Servidor"
def obter_informacoes_servidor(message):
    dados_usuario[message.chat.id]['servidor_nome_completo'] = message.text
    bot.send_message(message.chat.id, "Agora, descreva o problema:")
    bot.register_next_step_handler(message, obter_problema_servidor)
# Função para obter o problema do usuário para a opção "Servidor"
def obter_problema_servidor(message):
    dados_usuario[message.chat.id]['servidor_problema'] = message.text
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_confirmar = types.InlineKeyboardButton(text='Confirmar', callback_data='servidor_confirmar')
    btn_cancelar = types.InlineKeyboardButton(text='Cancelar', callback_data='servidor_cancelar')
    markup.add(btn_confirmar, btn_cancelar)
    bot.send_message(message.chat.id, "Por favor, confirme se as informações estão corretas:", reply_markup=markup)





# SESSÃO DE [EMAIL]

# Função para iniciar o processo de coleta de informações para o e-mail
def iniciar_coleta_email(chat_id):
    template = (
        "Por favor, descreva as informações necessárias para configurar o email utilizando o template (⚠️ É necessário copiar e colar todo o texto abaixo):\n\n"
        "NOME COMPLETO:\nCARGO:"
    )
    bot.send_message(chat_id, template, parse_mode='Markdown')
    bot.register_next_step_handler_by_chat_id(chat_id, obter_informacoes_email) 
# Função para obter as informações do e-mail
def obter_informacoes_email(message):
    lines = message.text.split('\n')
    nome_completo, cargo = '', ''
    for line in lines:
        if 'NOME COMPLETO:' in line:
            nome_completo = line.replace('NOME COMPLETO:', '').strip()
        elif 'CARGO:' in line:
            cargo = line.replace('CARGO:', '').strip()
    
    if nome_completo and cargo:
        # Armazene as informações no dicionário dados_usuario
        dados_usuario[message.chat.id] = {
            'nome_completo': nome_completo,
            'cargo': cargo
        }
        enviar_mensagem_confirmacao_email(message.chat.id, nome_completo, cargo)
    else:
        bot.send_message(message.chat.id, "Por favor, forneça todas as informações solicitadas.")
# Função para enviar mensagem de confirmação de e-mail
def enviar_mensagem_confirmacao_email(chat_id, nome_completo, cargo):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_confirmar = types.InlineKeyboardButton(text='Confirmar', callback_data='confirmar_email')
    btn_cancelar = types.InlineKeyboardButton(text='Cancelar', callback_data='cancelar_email')
    markup.add(btn_confirmar, btn_cancelar)
    bot.send_message(chat_id, f"Confirma o envio das informações de email?\n\nNOME COMPLETO: {nome_completo}\nCARGO: {cargo}", reply_markup=markup)
# Handlers para confirmação de e-mail
@bot.callback_query_handler(func=lambda call: call.data in ['confirmar_email', 'cancelar_email'])
def callback_query_confirmar_email(call):
    if call.data == 'confirmar_email':
        # Obtém nome completo e cargo do usuário a partir dos dados armazenados
        nome_completo = dados_usuario[call.message.chat.id]['nome_completo']
        cargo = dados_usuario[call.message.chat.id]['cargo']
        
        # Envia mensagem de agradecimento e pedido de aguardar
        bot.send_message(call.message.chat.id, "Obrigado! Por favor, aguarde enquanto processamos suas informações.")
        
        # Envia mensagem de confirmação para chat específico
        enviar_mensagem_chats(["-1002125287134"], f"[EMAIL]: {call.message.chat.username}\n\n➔ NOME COMPLETO: {nome_completo}\n➔ CARGO: {cargo}", call.message.chat.id)
    elif call.data == 'cancelar_email':
        # Envia mensagem de cancelamento
        bot.send_message(call.message.chat.id, "Solicitação de email cancelada. Obrigado!")




# SESSÃO DE [FUNCIONALIDADES GERAL]

# Função para enviar mensagem para os chats específicos, excluindo o chat_id do usuário
def enviar_mensagem_chats(chat_ids, mensagem, chat_id_usuario):
    for chat_id in chat_ids:
        if str(chat_id) != str(chat_id_usuario):
            bot.send_message(chat_id, mensagem)
# Função para enviar a mensagem para o grupo indicado
def enviar_mensagem_grupo(chat_id, mensagem):
    # Enviar a mensagem para o grupo específico
    bot.send_message("-1002125287134", mensagem)
    
bot.polling()
