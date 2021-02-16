# lang=	update._effective_user.language_code
# d['qr'][0][lang]
# print d['IMC']['TITLE']['es']

d={
'ERR':{
	'config':{
		'en':"[{}] Not found. Define it in a file called [bot.conf].",
		'es':"[{}] No encontrada. Puede definirla en el fichero [bot.conf]."
	}
},
'help':{
	'title':{
		'en':"📃 <b>Command list</b>\n▬▬▬▬▬▬▬▬▬▬▬▬\n",
		'es':"📃 <b>Lista de comandos</b>\n▬▬▬▬▬▬▬▬▬▬▬▬\n"
	},
	'commands':[
		{
			'en':"/help - 📃 Command list\n",
			'es':"/help - 📃 Lista de comandos\n"
		},{
			'en':"/coin - ⚪️/⚫️ Heads or tails\n",
			'es':"/coin - ⚪️/⚫️ cara o cruz\n"
		},{
			'en':"/qr - 🏁 Generate QR code\n",
			'es':"/qr - 🏁 Genera código QR\n"
		}
	]
},
'qr':{
	'title':{
		'en':"🏁 <b>QR</b>\n▬▬▬▬▬▬▬▬▬▬▬▬\n",
		'es':"🏁 <b>QR</b>\n▬▬▬▬▬▬▬▬▬▬▬▬\n"
	},
	'enun':{
		'en':"<i>Now insert URL or text to generate a QR code.</i>\n\n /cancel",
		'es':"<i>Inserta ahora la URL o texto, para generar el código.</i>\n\n /cancel "
	},
},
'coin':{
	'head':{
		'en':"⚪ Head",
		'es':"⚪ Cara"
	},
	'tail':{
		'en':"⚫️ Tail",
		'es':"⚫️ Cruz"
	},
}
}


#print d['IMC']['TITLE']['es']
