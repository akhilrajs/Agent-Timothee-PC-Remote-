# Agent Timothee ( PC Remote)
>A telegram BOT written in python to remote control your PC
# This is just a concept i have , still working on it !!!
## Basic code for Telegram BOT
###### Basic code to read what the user sends to the Telegram BOT by ChatGPT
```python
import telebot

# create a new bot using the token provided by the Telegram Bot Father
bot = telebot.TeleBot("YOUR_BOT_TOKEN")

# define a function that will be called when a message is received
@bot.message_handler(content_types=['text'])
def handle_message(message):
    print("Received message:", message.text)
    bot.send_message(message.chat.id, "Thank you for your message!")

# start the bot
bot.polling()

```
## Code to run the messages in Terminal 
```python
import subprocess

def run_in_terminal(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        print("Error: ",stderr.decode())
    else:
        print(stdout.decode())

user_input = input("Please enter a command to run in the terminal: ")
run_in_terminal(user_input)
```

> First, i need the program to run the commands send by the user in terminal and send that back to the user 
