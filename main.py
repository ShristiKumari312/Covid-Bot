import json
import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token= '6134637878:AAECpACxHk1WItr_DSE2aCHm4ZiaXxkUjm0',use_context=True)
dispatcher = updater.dispatcher
def summary(update, context):
    response= requests.get('https://api.covid19api.com/summary')
    if(response.status_code == 200):
        data = response.json()
        date = data['Date'][:10]
        ans=f'Covid 19 Summary (as of {date}): \n';
        for attribute,value in data['Global'].items():
            if attribute not in ['NewConfirmed', 'NewDeaths', 'NewRecovered']:
                ans += 'Total'+ attribute[5::].lower()+":"+ str(value)+ "\n"
        print(ans)
        context.bot.send_message(chat_id=update.effective_chat.id,text=ans)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,text='Something went wrong.')

    
command_handler=CommandHandler('Summary',summary)
dispatcher.add_handler(command_handler)
updater.start_polling()