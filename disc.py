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
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        tmp = await client.send_message(message.channel, 'ZzZ...')
        await asyncio.sleep(5)
        await client.edit_message(tmp, 'Done sleeping')

client.run("MzEyNDg5ODQyMTI0NTIxNDcy.C_b8OA.RL5BrCK2ycVzuGX_--QUA0IhpTQ")
