# bot.py

import discord
import random
import os
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

	for guild in client.guilds:
		if guild.name == GUILD:
			break

	print(
		f'{client.user} is connected to the following guild:\n'
		f'{guild.name}(id: {guild.id})'
	)

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	inspirational_quotes = [
		'Act as if what you doe makes a difference. IR DOES. - William James',
		'Believe you can and you\'re halfway there. - Theodore Roosevelt',
		(
			'Wow. Wow wow wow wow wow wow wow '
			'doubt doubt doubt doubt.'
		),
	]

	bee_movie_quotes = [
		'According to all known laws of aviation, there is no way a bee should be able to fly.',
		'Ya like jazz?',
		'He happens to be the nicest bee I\'ve met in a long time',
		'That bee is living my life!',
	]

	if message.content == 'bee!':
		#response = random.choice(inspirational_quotes)
		response = random.choice(bee_movie_quotes)
		await message.channel.send(response)

client.run(TOKEN)
