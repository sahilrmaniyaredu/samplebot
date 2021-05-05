import chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer    
chatbot = ChatBot(
    'Nitr Chatbot',  
     )

from chatterbot.trainers import ListTrainer

while True:
    try:
        user_input = input("you:")
        chatbot_response=chatbot.get_response(user_input)
        print("NITRbot:",chatbot_response)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break

