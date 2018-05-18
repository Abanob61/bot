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
        await client.change_presence(game=discord.Game(name="Pes6Stars.cf"), status=discord.Status("online"))
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!status'):
        embed = discord.Embed(title="Pes6stars bot", description="Nicest bot there is ever.", color=0xeee657)
    
        # give info about you here
        embed.add_field(name="Author", value="Bob")

        # give users a link to invite thsi bot to their server
        embed.add_field(name="Invite", value="[Invite link](<https://discordapp.com/invite/fF5KZsw>)")

        await client.send_message(message.channel, embed=embed)      
        

client.run('NDQ2NzYyNTAyOTQ1MTEyMDc1.Dd9vrA.JJH1dpg-64cIdQby0uzfZryhpaU')