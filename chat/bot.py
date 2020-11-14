import os
import threading
import discord
from dotenv import load_dotenv
from googlesearch import search
from chat.models import Bot, Trigger
from chat.recent_history import store_history, history
import psycopg2
def run_bot():
    load_dotenv()
    histories = []
    #I have stored token and server name in .env file for ease of login
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')
    client = discord.Client()
    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
            
                print("guild Name = %s and id = %s"%(guild.name,guild.id))
                break
        print(f'{client.user} has connected to Discord!')

    #Here I have handled all the cases, like what to reply when I get Hi or !google or !recent
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        if message.content.lower() == 'hi':
            await message.channel.send('Hey')

        # If I get message starting with !recent I will extract '!google' from the message and process other part
        # of the message content
        if message.content.lower().split()[0] == '!google':
            messages = message.content.lower()[7:]
            if len(messages) == 0:
                await message.channel.send("Enter Valid Query")
                pass #continue
            for j in search(message.content.lower()[7:], tld="co.in", num=5, stop=5, pause=2):
                await message.channel.send(j)
            second = threading.Thread(target=store_history,args=(messages,))
            second.start()
        # If I get message starting with !recent I will extract '!recent' from the message and process other part
        # of the message content
        if message.content.lower().split()[0] == '!recent':
            name_of_query = message.content.lower()[7:]#.split()[1]
            ans = history(name_of_query)
            result = ans.result_queue.get()
            for recent in result:
                await message.channel.send(recent)#[0].history)

    client.run(TOKEN)

#run_bot()
'''trigger = Trigger.objects.all()
print(trigger)
if trigger.is_enabled:
    run_bot()
'''
