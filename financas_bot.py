import telebot

CHAVE_API = '6493137670:AAHBijEnyT4QKfiyzEDb5q-X-M_jlraWSao'
bot = telebot.TeleBot(CHAVE_API)

orcamento_semanal = 0.0

@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    
    texto = """
Ok! Para qual valor você deseja atualizar? Use "." em vez de "," caso seja um valor quebrado. (exemplo: 142.5)
"""
    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    pass

@bot.message_handler(func= lambda _: True)
def responder(mensagem):

    print(mensagem)

    user_name = mensagem.from_user.first_name

    texto_inicial =  f'''
Olá, {user_name}! Meu nome é Finanças. Vou te ajudar a controlar melhor seu dinheiro no decorrer da semana. Segundo meu banco de dados, seu orçamento semanal atual está no valor de R$ {orcamento_semanal}
    
    Para iniciarmos, clique em um dos itens abaixo:
    /opcao1 Atualizar o valor do seu orçamento semanal
    /opcao2 Adicionar algum gasto

⚠ Responder qualquer outra coisa não vai funcionar.
    '''

    bot.reply_to(mensagem, texto_inicial)

bot.polling()
