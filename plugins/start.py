def start(update, context):
	setLang(update)
	cid=update.message.chat_id
	msg="<i>Hola.</i>"
	context.bot.send_message(cid, msg, parse_mode=ParseMode.HTML)