import telebot

CHAVE_API = '6493137670:AAHBijEnyT4QKfiyzEDb5q-X-M_jlraWSao'
bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(func= lambda msg: True)
def responder(mensagem):

    texto_inicial =  '''
Olá, aqui é o Bot de Finanças criado por Ramon Nery. Vou te ajudar a controlar melhor seu dinheiro no decorrer da semana.
    
    Para iniciarmos, clique em um dos itens abaixo:
    /opcao1 Atualizar o valor de seu orçamento semanal
    /opcao2 Adicionar algum gasto

⚠ Responder qualquer outra coisa não vai funcionar.
    '''

    bot.reply_to(mensagem, texto_inicial)

bot.polling()
