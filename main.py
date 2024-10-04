# Description: This is a simple script to send messages to a telegram channel using the Telegram Bot API and Python.

import asyncio,telegram,os
from dotenv import load_dotenv

load_dotenv()
apikey=os.getenv("BOTAPIKEY")
channel_id=os.getenv("CHATID")

# Create a Bot Object
bot = telegram.Bot(token=apikey)


# Function to send messages
async def send_message(message):
    await bot.send_message(chat_id=channel_id, text=message)

# Function to for sending the messages
def main():
    loop = asyncio.get_event_loop()
    message="Testing Message from Python" # You can change the message in Here  
    loop.run_until_complete(send_message(message))

if __name__ == "__main__":
    main()