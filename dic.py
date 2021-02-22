# lang=	update._effective_user.language_code
# d['qr'][0][lang]
# print d['IMC']['TITLE']['es']

d={
'LANGUAGES':['en','es']
,'ERR':{
	'config':{
		'en':"[{}] Not found. Define it in a file called [bot.conf].",
		'es':"[{}] No encontrada. Puede definirla en el fichero [bot.conf]."
	}
},'start':{
	'title':{
		'en':"📃 <b>Tools_bot</b>\n▬▬▬▬▬▬▬▬▬▬▬▬\n",
		'es':"📃 <b>Tools_bot</b>\n▬▬▬▬▬▬▬▬▬▬▬▬\n"
	},
	'text':{
		'en':"<i>Welcome\nThen the list of tasks available in the bot will appear.</i>\n",
		'es':"<i>Bienvenido\nA continuación te envío la lista de comandos disponibles en el bot.</i>\n"	
	}
},'help':{
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
	],
	'multim':[
		{
			'en':"🎵 <i>Send me an audio\nwith the song that you whant to know.</i>\n",
			'es':"🎵 <i>Envía un audio con la\ncanción que quieras conocer.</i>\n"	
		},{
			'en':"🖼 <i>Send a photo to remove the background .</i>\n",
			'es':"🖼 <i>Envía una foto para eliminar el fondo.</i>\n"	
		}
	],
},'qr':{
	'title':{
		'en':"🏁 <b>QR</b>\n▬▬▬▬▬▬▬▬▬▬▬▬\n",
		'es':"🏁 <b>QR</b>\n▬▬▬▬▬▬▬▬▬▬▬▬\n"
	},
	'enun':{
		'en':"<i>Now insert URL or text to generate a QR code.</i>\n\n /cancel",
		'es':"<i>Inserta ahora la URL o texto, para generar el código.</i>\n\n /cancel "
	},
},'song':{
	'title':{
		'en':"🎶 <b>SONG</b>\n▬▬▬▬▬▬▬▬▬▬▬▬\n",
		'es':"🎶 <b>SONG</b>\n▬▬▬▬▬▬▬▬▬▬▬▬\n"
	},
	'notfound':{
		'en':"<i>Song not found.</i>",
		'es':"<i>Canción no encontrada</i>"
	},
},'coin':{
	'head':{
		'en':"⚪ Head",
		'es':"⚪ Cara"
	},
	'tail':{
		'en':"⚫️ Tail",
		'es':"⚫️ Cruz"
	},
},'image':{
	'start':{
		'en':"🖼 <i>What you want to do?</i>",
		'es':"🖼 <i>¿Que quieres hacer?</i>"
	},'sending':{
		'en':"<i>Sending...</i>",
		'es':"<i>Enviando...</i>"
	},'button':{
		'delbackground':{
			'en':"Clean background",
			'es':"Borrar fondo"
		},
		'cancel':{
			'en':"❌ Cancel",
			'es':"❌ Cancelar"
		},
	},'error':{
		'400':{
			'en':"<i>❌ Error: Invalid parameters or input file unprocessable.</i>",
			'es':"<i>❌ Error: Parámetro válido o fichero no procesable.</i>"
		},
		'402':{
			'en':"<i>❌ Error: Limit reached\nContact the administrator.</i>",
			'es':"<i>❌ Error: Se ha llegado al límite\nContacte con el administrador.</i>"
		},
		'else':{
			'en':"<i>Some error has occurred.\nTry another photo </i>",
			'es':"<i>Algún error ha ocurrido.\nPrueba con otra foto</i>"
		},
	},
}
}
