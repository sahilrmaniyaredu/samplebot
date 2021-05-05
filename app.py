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
from chatbot import chatbot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    app.run() 
