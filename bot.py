import discord
import responses

async def send_message (message, user_message, is_public):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_public else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "MTE0NzMzNzk1ODkxNjEwNDI4Mw.GkIOr7.k5QIF0y0NPGN5akpWE32KLksvbmp7DgJUsyEtM"
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} ya esta funcionando :D')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} dijo: "{user_message}"({channel})')

        if user_message[0]  == '?':
            user_message = user_message[1:] 
            await send_message(message, user_message, is_public=True)
        else:
            await send_message(message, user_message, is_public=False)

    client.run(TOKEN)   


