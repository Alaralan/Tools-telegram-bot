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
───────────────────────────────────────────────────────────────────
🎵 Analiza el audio que se le envíe y te indica la canción.
🖼 Elimina el fondo de una foto enviada.
═════════════════════════════════════════════════════════════════════
■ DOC
· https://github.com/python-telegram-bot/python-telegram-bot/wiki/Transition-guide-to-Version-12.0#error-handler-callbacks
'''
#╔═══════════════════════════════════════════════════════════════════
#║ ■ IMPORTS
import sys, os, random, json, subprocess, requests
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, ForceReply)
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler,
													MessageHandler, Filters, ConversationHandler)
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
""" Download MP3 from youtube"""
import youtube_dl
#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
from pprint import pprint
# pprint(update.to_dict())
#╔═══════════════════════════════════════════════════════════════════
#║ ■ DIC
from dic import d
lang='en';
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

	TEMP=config.get('PATH', 'temp') if CheckConfFile('PATH', 'temp') else "None"

	TOKENSONG=config.get('TOKEN', 'song') if CheckConfFile('TOKEN', 'song') else "None"
	TOKENIMG=config.get('TOKEN', 'img') if CheckConfFile('TOKEN', 'img') else "None"
	TOKENIMG2=config.get('TOKEN', 'img2') if CheckConfFile('TOKEN', 'img2') else "None"
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
def setLang(update):
	global lang
	try:
		lang=update._effective_user.language_code
		if lang not in d['LANGUAGES']:
			lang='en'
	except:
		lang='en'
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def button(update, context):
	setLang(update)
	query = update.callback_query

	if query.data.split('_',1)[0]=='img':
		img_bt(update, context)
	elif query.data.split('_',1)[0]=='0':
		msg=d['image']['button']['cancel'][lang]
		context.bot.edit_message_text(msg, query.message.chat_id, query.message.message_id, parse_mode=ParseMode.HTML)
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def start(update, context):
	setLang(update)
	cid=update.message.chat_id
	# msg=d['start']['title'][lang]
	msg=d['start']['text'][lang]
	context.bot.send_message(cid, msg, parse_mode=ParseMode.HTML)
	helpC(update, context)
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def helpC(update, context):
	''' HELP '''
	setLang(update)
	cid=update.message.chat_id
	msg=d['help']['title'][lang]
	for i in d['help']['commands']:
		msg+=i[lang]
	for i in d['help']['multim']:
		msg+="───────────────\n"
		msg+=i[lang]

	context.bot.send_message(cid, msg, parse_mode=ParseMode.HTML)
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def coin(update, context):
	''' ⚪️/⚫️ Moneda '''
	setLang(update)
	cid=update.message.chat_id
	v_coin=random.randint(1,2)
	msg=d['coin']['head'][lang] if v_coin==1 else d['coin']['tail'][lang]
	update.message.reply_text(msg)
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def qr(update, context):
	''' QR '''
	setLang(update)
	if update.message.text[4:].strip()=='':
		msg=d['qr']['title'][lang]
		msg+=d['qr']['enun'][lang]
		MessageHandler(Filters.text, qr, pass_user_data=True)
		update.message.reply_text(msg, parse_mode=ParseMode.HTML)
		return CHOOSING
	else:
		qr_resul(update, context)
def qr_resul(update, context):
	setLang(update)
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
	setLang(update)
	# ayuda(update, context)
	return ConversationHandler.END
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def f_audio(update, context):
	''' SONG '''
	setLang(update)
	msg=d['song']['title'][lang]
	tempSong=TEMP+"song.ogg"
	context.bot.send_chat_action(update.message.chat.id, 'typing') # typing...

	# Download in /tmp/song.ogg
	file_download=context.bot.get_file(update.message.voice.file_id)
	file_download.download(tempSong)

	process=subprocess.run(['curl','--silent','-F','api_token='+TOKENSONG+'','-F','file=@'+tempSong+'','https://api.audd.io/'], capture_output=True)
	v_song=json.loads(process.stdout)

	if v_song['result']!=None:
		if v_song['status']=='success':
			msg+='<code>{} - {}</code>'.format(v_song['result']['artist'], v_song['result']['title'])
	else:
		msg+=d['song']['notfound'][lang]

	update.message.reply_text(msg, parse_mode=ParseMode.HTML)
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def img_start(update, context):
	''' BACKGROUND REMOVE '''
	setLang(update)
	file_id=update.message.photo[len(update.message.photo)-1].file_id
	msg=d['image']['start'][lang]
	keyboard = [[InlineKeyboardButton(d['image']['button']['delbackground'][lang], callback_data='img_background'),
				 InlineKeyboardButton(d['image']['button']['cancel'][lang], callback_data='0')],
	]
	update.message.reply_text(msg, parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(keyboard),reply_to_message_id=update.message.message_id)
def img_bt(update, context):
	setLang(update)
	query=			update.callback_query
	chat_id=		query.message.chat_id
	message_id=	query.message.message_id

	context.bot.edit_message_text(d['image']['sending'][lang], chat_id, message_id, parse_mode=ParseMode.HTML)
	context.bot.send_chat_action(chat_id, 'typing')

	if query.data.split('_',1)[1]=='background':
		file_id=query.message.reply_to_message.photo[len(query.message.reply_to_message.photo)-1].file_id

		# Descarga
		file_photo=context.bot.get_file(file_id)
		file_photo.download(TEMP+str(chat_id)+'.jpg')

		# Elimina el fondo y lo almacena para enviar
		status=img_background_rm(TEMP+str(chat_id))
		if status==200:
			# Envía
			photo=open(TEMP+str(chat_id)+'.png', 'rb')
			context.bot.delete_message(chat_id, message_id)
			context.bot.send_document(chat_id, photo, reply_to_message_id=message_id-1)
		elif status==400:
			context.bot.edit_message_text(d['image']['error']['400'][lang], chat_id, message_id, parse_mode=ParseMode.HTML)
		elif status==402:
			context.bot.edit_message_text(d['image']['error']['402'][lang], chat_id, message_id, parse_mode=ParseMode.HTML)
		else:
			context.bot.edit_message_text(d['image']['error']['else'][lang], chat_id, message_id, parse_mode=ParseMode.HTML)
		subprocess.run(['rm','-f',TEMP+str(chat_id)+'.png'])
def img_api(img, token):
	'''==[ Background Removal ]=='''
	return requests.post(
		'https://api.remove.bg/v1.0/removebg',
		files={'image_file': open(img+'.jpg', 'rb')},
		data={'size': 'regular'},
		headers={'X-Api-Key': token},
	)
def img_background_rm(img):
	response=img_api(img, TOKENIMG)
	if response.status_code==requests.codes.ok:
		with open(img+'.png', 'wb') as out:
			out.write(response.content)
	elif response.status_code!=requests.codes.ok:
		response=img_api(img, TOKENIMG2)
		if response.status_code==requests.codes.ok:
			with open(img+'.png', 'wb') as out:
				out.write(response.content)
	return response.status_code
#▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
def you2mp3(update, context):
	setLang(update)

	if update.message!=None and update.message.chat.type=='private':
		url=update.message.text;
		cid=update.message.chat.id
		mid=update.message.message_id
	elif update.channel_post.sender_chat.type=='channel':
		url=update.channel_post.text;
		cid=update.channel_post.sender_chat.id
		mid=update.channel_post.message_id

	context.bot.send_chat_action(cid, 'typing') # Enviando ...
	msg=d['youtube']['send'][lang]
	context.bot.send_message(cid, msg, parse_mode=ParseMode.HTML)
	
	# Download
	ydl_opts={
		'format': 'bestaudio/best',
		'outtmpl': '%(title)s.%(ext)s',
		'noplaylist' : True,
		'continue_dl' : True,
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192',
		},
		{'key': 'FFmpegMetadata'},
		],
		# 'progress_hooks': [my_hook],
	}
	try:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			song_title=ydl.extract_info(url,download=False)['title']
			ydl.download([url])
		song_file=open(song_title+'.mp3', 'rb')
		context.bot.send_document(cid, song_file)
		os.remove(song_title+'.mp3')
		try:
			# Evita el error si el bot no tiene permisos para borrar.
			context.bot.delete_message(cid, mid)
		except:
			pass
		context.bot.delete_message(cid, mid+1)
	except Exception:
		context.bot.delete_message(cid, mid+1)
		msg=d['youtube']['err'][lang]
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
	
	dp.add_handler(MessageHandler(Filters.regex(r"((http(s)?:\/\/)?)(www\.)?((youtube\.com\/)|(youtu.be\/))[\S]+"), you2mp3))
#__________________________________________________________________
#│ Multimedia
	if TOKENSONG!="None":
		dp.add_handler(MessageHandler(Filters.photo, img_start))
	if TOKENIMG!="None":
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
	dp.add_handler(CallbackQueryHandler(button))
#════════════════════════════════════════════════════════════════════
	dp.add_error_handler(error_callback)
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	print(('['+BOTNAME+'] Start...'))
	main()
