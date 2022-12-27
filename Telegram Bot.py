# SIMPLE TELEGRAM BOT in BAHASA INDONESIA
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

def main():
    #API used in this program supplied by telegram BotFather
    api = "5974769977:AAEPQFDx0TQgKRkZFCafu_z6xhOtrdhHZ-o"
    updater = Updater(api, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))              #creating "MULAI" button as start button to star the bot
    dp.add_handler(MessageHandler(Filters.text, reply))
    updater.start_polling()
    updater.idle()

#creating start function to throw reply after user click "MULAI" button
def start(update:Update, context:CallbackContext) -> None:
    update.message.reply_text("Ada perlu apa?")             #throwing first reply after user click on the start button

#creating reply function, this function use for handling the reply for user input
def reply(update: Update, context: CallbackContext) -> None:
    query = update.message.text.lower()             #all the user input will be converted as lower so it will detected by the replies dictionary
    user_name = update.effective_user.first_name
    #save the user input chat as key and the answer as value in replies dictionary
    replies = {
        "hi" : f"Halo, {user_name}",
        "halo" : f"Hi, {user_name}",
        "assalamualaikum" : "Waalaikumsalam",
        "bagaimana kabarmu?" : "Kabarku baik, terimakasih.",
        "siapa namamu?" : "Namaku Muhammad Adnan Bayu Firdaus",
        "kamu biasa dipanggil siapa?" : "Anda bisa memanggil saya Bayu",
        "selamat tinggal" : "Sampai jumpa!"
    }
    for key, value in replies.items():
        if query in key:
            update.message.reply_text(value)
            break
    else:
        update.message.reply_text("Maaf saya tidak mengerti maksud kalimat anda")               #if the user input chat isn't in replies dictionary, this exception message will thrown

if __name__ == "__main__":
    main()

#open the bot on this link : https://t.me/adnan_bayu_telegram_bot