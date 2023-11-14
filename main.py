import telebot

CHAVE_API = '6493137670:AAHBijEnyT4QKfiyzEDb5q-X-M_jlraWSao'
bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(func=lambda _: True)
def responder(mensagem):
    global orcamento_semanal
    print(mensagem)
    user_name = mensagem.from_user.first_name

    texto_inicial =  f'''
Olá, {user_name}! Meu nome é Finanças. Vou te ajudar a controlar melhor seu dinheiro no decorrer da semana. Segundo meu banco de dados, seu orçamento semanal atual está no valor de R$ {orcamento_semanal}
    
    Para iniciarmos, clique em um dos itens abaixo:
    /Atualizar o valor do seu orçamento semanal
    /Adicionar algum gasto
    /Finalizar operação

⚠ Responder qualquer outra coisa não vai funcionar.
    '''

    bot.send_message(mensagem.chat.id, texto_inicial)

bot.polling()
