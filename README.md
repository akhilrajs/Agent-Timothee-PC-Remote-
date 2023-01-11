# Agent Timothee ( PC Remote)
>A telegram BOT written in python to remote control your PC

## Basic code for Telegram BOT
###### Basic code to read what the user sends to the Telegram BOT by ChatGPT
```
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
