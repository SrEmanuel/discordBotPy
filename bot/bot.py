#start
import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()

@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord!\n'
              f'and has connected to these servers:'
            )
        for guild in client.guilds:
            print(
                f'{guild.name} || ID: {guild.id} || Membros: {guild.member_count}'
            )

@client.event
async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Fala aí, {member.name}, seja bem-vindo ao meu servidor discord!'
        )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    orion = [
        'Que!? Que nome estranho... Eu hein 👀',
        'Esse nome me parece familiar....',
        'Vai dar ruim.',
    ]

    if message.content == 'Orion Quest':
        response = random.choice(orion)
        await message.channel.send(response)

    if message.content == 'Quem é o Super Xandão?':
        await message.channel.send('A última salvação da terra. Uma criação divina. A única pessoa que pode nos salvar no fim dos tempos')

    if message.content == 'Me mostra teus comandos Sr':
        await message.channel.send('O preguiçoso quem fez esse bot mal escrito e de péssima qualidade, só implementou resposta as seguintes mensagens:\n'
        'Quem é o Super Xandão?\n'
        'Orion Quest\n'
        'Me mostra teus comandos Sr')

client.run(TOKEN)