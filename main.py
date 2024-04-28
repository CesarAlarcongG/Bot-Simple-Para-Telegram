import telebot

#Token obtenido de BotFather
TOKEN ='AQUI_TOKEN' #Remplaza este código

#Creamos una instancia de bot y conección a telegram
bot = telebot.TeleBot(TOKEN)

#Crear comando '/help'
@bot.message_handler(commands=['help'])

def enviar_help(message):
    bot.reply_to(message, 'Mensaje de comando') #Remplaza este mensaje

#Crear comando '/roadmap'
@bot.message_handler(commands=['roadmap'])

def envia_roadmap(message):
    bot.reply_to(message, 'Mensaje de comando') #Remplaza este mensaje



#Iniciamos el bot
if __name__ == "__main__":
    bot.polling(none_stop= True)
