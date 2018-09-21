from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

import codecs

bot = ChatBot('test')

dialogo_inicial = list(codecs.open("dialogo_inicial.txt", "r", encoding="utf-8"))

bot.set_trainer(ListTrainer)
bot.train(dialogo_inicial)

while True:
	question = input("Você: ")
	answer = bot.get_response(question)

	# O bot só responderá quando a confiabilidade de resposta for um pouco maior
	if float(answer.confidence) > 0.5:
		print("Bot: ", answer)
	else:
		print("Bot: Eu não sei.")
	