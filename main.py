import telebot

#Token obtenido de BotFather
TOKEN ='7022399311:AAEwibGGtU1rxqUv44KDk6HCVulbovGW5qg' #Remplaza este código

#Creamos una instancia de bot y conección a telegram
bot = telebot.TeleBot(TOKEN)



#Crear comando '/roadmap'
@bot.message_handler(commands=['roadmap'])

def envia_roadmap(message):
    bot.reply_to(message, 'Mensaje de roadmap')


#Crear comando '/help'
@bot.message_handler(commands=['help'])

def enviar_help(message):
    bot.reply_to(message, 'Comandos: /n/roadmap = Muesta la ruta de aprendizaje que seguiremos en el grupo')


#Iniciamos el bot
if __name__ == "__main__":
    bot.polling(none_stop= True)
