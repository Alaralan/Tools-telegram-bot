#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''	🌕🌖🌗🌘🌑 Nidea 🌑🌒🌓🌔🌕
═════════════════════════════════════════════════════════════════════
Alan tools bot
Alan_tools_bot
───────────────────────────────────────────────────────────────────
Bot que gestion varias herramientas.
───────────────────────────────────────────────────────────────────
help - Lista de comandos
coin - Tira una moneda al aire
qr - Genera un código QR
═════════════════════════════════════════════════════════════════════
■ DOC
· https://github.com/python-telegram-bot/python-telegram-bot/wiki/Transition-guide-to-Version-12.0#error-handler-callbacks
'''
#╔═══════════════════════════════════════════════════════════════════
#║ ■ IMPORTS
import sys, os, random, json, subprocess
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, ForceReply)
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler,
													MessageHandler, Filters, ConversationHandler)
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
from pprint import pprint
# pprint(update.to_dict())
#╔═══════════════════════════════════════════════════════════════════
#║ ■ DIC
from dic import d
lang='es';
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
def ErrorManager(param):
	sys.exit(d['error']['config']['es'].format(param))
def CheckConfFile(categ, param):
	if config.has_option(categ, param) and config.get(categ,param)!="":
		return True
	else:
		return False
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
# • Cargar fichero de configuración
TOKEN=""
FPATH=os.path.dirname(os.path.abspath(__file__))
FCONF=os.path.join(FPATH,'bot.conf')
if os.path.isfile(FCONF):
	import configparser
	config=configparser.ConfigParser()
	config.sections()
	config.read(FCONF)

	TOKEN=config.get('DEFAULTS', 'token') if CheckConfFile('DEFAULTS','token') else ErrorManager("token")
	BOTNAME=config.get('DEFAULTS', 'name') if CheckConfFile('DEFAULTS', 'name') else "UNKNOW"
	TEMP=config.get('PATH', 'temp') if CheckConfFile('PATH', 'temp') else null
else:
	sys.exit("No config file found. Remember changing the name of bot-sample.conf to bot.conf")
#╔═══════════════════════════════════════════════════════════════════
#║ ■ LOGS	♦ https://docs.python.org/2/howto/logging.html
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def start(update, context):
	cid=update.message.chat_id
	msg="<i>Hola.</i>"
	context.bot.send_message(cid, msg, parse_mode=ParseMode.HTML)
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def helpC(update, context):
	''' HELP '''
	cid=update.message.chat_id
	msg=d['help']['title'][lang]
	for i in d['help']['commands']:
		msg+=i[lang]
	msg+="▬       ▬       ▬       ▬       ▬\n"
	msg+=d['help']['multim'][lang]
	
	context.bot.send_message(cid, msg, parse_mode=ParseMode.HTML)
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def coin(update, context):
	''' ⚪️/⚫️ Moneda '''
	cid=update.message.chat_id
	v_coin=random.randint(1,2)
	msg=d['coin']['head'][lang] if v_coin==1 else d['coin']['tail'][lang]
	update.message.reply_text(msg)
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def qr(update, context):
	''' QR '''
	if update.message.text[4:].strip()=='':
		msg=d['qr']['title'][lang]
		msg+=d['qr']['enun'][lang]
		MessageHandler(Filters.text, qr, pass_user_data=True)
		update.message.reply_text(msg, parse_mode=ParseMode.HTML)
		return CHOOSING
	else:
		qr_resul(update, context)
def qr_resul(update, context):
	if update.message.text.strip()!='':
		cid=update.message.chat.id
		mid=update.message.message_id

		if update.message.text[:3]=='/qr':
			data=update.message.text[4:].strip()
		else:
			data=update.message.text.strip()
			context.bot.delete_message(cid, mid-1)
		context.bot.send_chat_action(update.message.chat.id, 'typing') # Enviando ...
		imageqr='https://api.qrserver.com/v1/create-qr-code/?size=250x250&data='+data
		context.bot.sendPhoto(cid, imageqr,'🏁 <code>{}</code>'.format(data), parse_mode=ParseMode.HTML)
		return ConversationHandler.END
def qr_exit(update, context):
	# ayuda(update, context)
	return ConversationHandler.END
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def f_audio(update, context):
	''' SONG '''
	msg=d['song']['title'][lang]
	tempSong=TEMP+"song.ogg"
	context.bot.send_chat_action(update.message.chat.id, 'typing') # typing...

	# Download in /tmp/song.ogg
	file_download=context.bot.get_file(update.message.voice.file_id)
	file_download.download(tempSong)

	# Get song name
	# v_song=json.load(requests.post(
		# 'https://api.audd.io/',
		# files={'image': tempSong},
		# headers={'api_token': 'test'},
	# ))
	# print(v_song)
	# v_song=json.loads(commands.getoutput('curl --silent -F "api_token=test" -F "file=@'+tempSong+'" https://api.audd.io/'))
	process=subprocess.run(['curl','--silent','-F','api_token=test','-F','file=@'+tempSong+'','https://api.audd.io/'], capture_output=True)
	v_song=json.loads(process.stdout)
	
	print("\n\n\n\n")
	print(v_song)
	print("\n")
	print(v_song['result'])
	print("\n")
	print(v_song['result']['artist'])

	if v_song['result']!=None:
		if v_song['status']=='success':
			msg+='<code>{} - {}</code>'.format(v_song['result']['artist'], v_song['result']['title'])
	else:
		msg+=d['song']['notfound'][lang]
	
	update.message.reply_text(msg, parse_mode=ParseMode.HTML)
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
#█ ■ main
CHOOSING, ADDING0, ADDING1 = list(range(3))
def main():
	updater=Updater(TOKEN, use_context=True)
	dp=updater.dispatcher
#__________________________________________________________________
#│ /Comandos_básicos
	dp.add_handler(CommandHandler('start',	start))
	dp.add_handler(CommandHandler('help',		helpC))
	dp.add_handler(CommandHandler('coin',		coin))
#__________________________________________________________________
#│ Multimedia
	dp.add_handler(MessageHandler(Filters.voice , f_audio))
#__________________________________________________________________
#│ Conversación
	conv_qr = ConversationHandler(
		entry_points=[CommandHandler('qr', qr)],

		states={
			CHOOSING:	[MessageHandler(Filters.text, qr_resul, pass_user_data=True),],
		},
		fallbacks=[CommandHandler('cancel', qr_exit, pass_user_data=True)]
	)
	dp.add_handler(conv_qr)
#__________________________________________________________________
#│ BOTON
	# dp.add_handler(CallbackQueryHandler(button))
#════════════════════════════════════════════════════════════════════
	dp.add_error_handler(error_callback)
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	print(('['+BOTNAME+'] Start...'))
	main()
