import discord
import asyncio
import random

client = discord.Client()

ROLES = {"Bite suprême": 12,"Gardien de la bite": 10, "@everyone": 0}

def getPoids(user):
    poids = 0
    for role in user.roles:
        if role.name in ROLES:
            if ROLES[role.name] > poids:
                poids = ROLES[role.name]
    return poids

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(discord.__version__)

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        send_typing(message.channel)
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        tmp = await client.send_message(message.channel, 'ZzZ...')
        await asyncio.sleep(5)
        await client.edit_message(tmp, 'Done sleeping')
    elif message.content.startswith('!bite'):
        meters = random.randint(0,1)
        centimeters = random.randint(1,99)
        bite = "8"
        tot = 100*meters + centimeters
        for i in range(tot//20):
            bite = bite + "="
        bite = bite + "D"
        await client.send_message(message.channel, 'Ta bite mesure {} metre {} en ce moment \n{}'.format(meters,centimeters, bite))
    elif message.content.startswith('!status'):
        name = message.content.split(" ")
        sep = " "
        name = sep.join(name[1:])
        gameBot = discord.Game()
        gameBot.name = name
        await client.change_presence(game = gameBot)
        #print(client.user.status)
        await client.send_message(message.channel, "Et ça m'amuse de jouer à {}".format(name))
    elif message.content.startswith('!kick'):
        name = message.content.split(" ")
        sep = " "
        name = sep.join(name[1:])
        member = None
        for user in client.get_all_members():
            if user.name + "#" +user.discriminator == name:
                member = user
        if member != None:
            if getPoids(member) >= getPoids(message.author):
                await client.send_message(message.channel, "Vous n'avez pas le droit de kicker {} ({})".format(name, getPoids(message.author)))
            else:
                await client.kick(member)
        else:
            await client.send_message(message.channel, "{} n'a pas été trouvé".format(name))
    elif message.content.startswith('!ban'):
        name = message.content.split(" ")
        sep = " "
        name = sep.join(name[1:])
        member = None
        for user in client.get_all_members():
            if user.name + "#" +user.discriminator == name:
                member = user
        if member != None:
            if getPoids(member) >= getPoids(message.author):
                await client.send_message(message.channel, "Vous n'avez pas le droit de bannir {} ({})".format(name, getPoids(message.author)))
            else:
                await client.ban(member)
        else:
            await client.send_message(message.channel, "{} n'a pas été trouvé".format(name))    
    elif message.content.startswith('!ninja'):
        pic = discord.Embed()
        pic.url = "http://www.dalerodgers.co.uk/wp-content/uploads/2015/08/ninja-computer-300x226.png"
        await client.send_message(message.channel, embed = pic)
         
    elif message.content.startswith("!help"):
        sep = "\n"
        msg = ("Menu d'aide:",
               "!test - Affiche le nombre de message postés dans le chan (max. 100)",
               "!sleep - Fait dormir le bot pendant 5 secondes",
               "!bite - Affiche la taille de votre bite",
               "!status [statut] - Change le jeu auquel le bot joue",
               "!kick [name] - Kick l'utilisateur demandé",
               "!ninja - Ninjaaa",
               "!help - Affiche toutes les commandes disponibles")
        await client.send_message(message.channel, sep.join(msg))

    if (message.content.find('bit') != -1) or (message.content.find('Bit') != -1):
        emobite = None
        for emoji in client.get_all_emojis():
            if emoji.name == "Bite":
                emobite = emoji
        chain = message.content.split(" ")
        if ("Bite" in chain) or ("Bit" in chain) or ("bite" in chain) or ("bit" in chain):
            await client.add_reaction(message, emobite)

@client.event
async def on_member_join(member):
    await client.send_message(member.server.get_channel("279533463772856320"), "Bienvenue {}, jeune padabite".format(member.name))

client.run("MzEzODAxNzU0NTgyMTg4MDMz.C_u6Rw.zSVUjqDomSc37LjdqpplpIIUe8w")
