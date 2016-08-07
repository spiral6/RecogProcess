import json
import re

import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    print('[Message]: ' + message.content)
    subreddit = re.match(r'/?r/(?P<name>\w+)', message.content)
    if subreddit is None:
        pass
    else:
        print(subreddit.group('name'))
        member = message.server.get_member(message.author.id)
        if message.server.id == config['server']:
            await client.send_message(message.channel,
                                      member.display_name + ' mentioned the specific subreddit: http://reddit.com/r/' + subreddit.group(
                                          'name'))


with open('process.conf') as data_file:
    config = json.load(data_file)

client.run(config['token'])
