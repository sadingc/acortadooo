from socket import timeout
import pyshorteners
from difflib import IS_LINE_JUNK
from cgitb import text
from fileinput import filename
from importlib.metadata import entry_points
from telegram.ext import Updater, CommandHandler, ConversationHandler,CallbackQueryHandler ,MessageHandler, Filters
from telegram import Chat, ChatAction, InlineKeyboardMarkup, InlineKeyboardButton, ReplyMarkup


INPUT_URL = 0

def url_callback_handler(update,context):
    
  query = update.callback_query
  query.answer()
  query.edit_message_text(
      text='**Enviame un 🔗Elace🔗 Acortarlo**'
  )
  return INPUT_URL 

def   help_comadhandler(update,context):
    update.message.reply_text(
        text='Usa el Boton 🔗Acortar Enlace🔗\nDespues envia un enlace para acortarlo\nReportar Errores con 😁**Mi Creador**😁@ELLP99'
    )
    return INPUT_URL
    


def inpunt_url(update, context):
    
    url = update.message.text
    chat = update.message.chat
    
    #Acortar URL
    
    s = pyshorteners.Shortener()
    short = s.chilpit.short('url')
   
    chat.send_action(
        action=ChatAction.TYPING,
       timeout=None
        
    )
    chat.send_message(
        text=short
       
    )

    return INPUT_URL
    
    
    
def start(update, context):
    
    update.message.reply_text(
        text= '🥳Hola Bienvenidos al 🤖Bot🤖\n\n❗️Usa el Comando /help Para Saber como funciona❗️',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='♨️ 🤩**Unirse al Canal**🤩 ♨️',url='https://t.me/bot_lewisDev')],
            [InlineKeyboardButton(text='😁**Mi Creador**😁',url='http://t.me/ELLP99/')],
            [InlineKeyboardButton(text='🔗Acortar Enlace🔗', callback_data='url')]
        ])
        
    )

def qr_comndhandler(update,context):
    update.message.reply_text('Enviame un texto para generar un codigo QR')
    return INPUT_URL


if __name__ == '__main__':

    updater = Updater(token='5591312951:AAE5m0GWHTVPCe-vJRbMTuDzZd9GG3xDtGg', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    
    dp.add_handler(CommandHandler('help', help_comadhandler))
    
    dp.add_handler(ConversationHandler(
        
        entry_points=[
            CallbackQueryHandler(pattern='url', callback=url_callback_handler)
            
            ],
        
        states={
            INPUT_URL: [MessageHandler(Filters.text, inpunt_url)]
            
            },
        
        fallbacks=[]
    ))

    updater.start_polling()
    
    print('El bot se esta ejecutando')

    updater.idle()



