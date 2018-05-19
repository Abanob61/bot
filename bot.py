import discord
import asyncio
import socket

client = discord.Client()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('pes6stars.cf',8190))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Pes6Stars.cf | !server-status"), status=discord.Status("online"))

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
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!status'):
        embed = discord.Embed(title="Pes6stars bot", description="Nicest bot there is ever.", color=0xeee657)
    
        # give info about you here
        embed.add_field(name="Author", value="Bob")

        # give users a link to invite thsi bot to their server
        embed.add_field(name="Invite", value="[Invite link](<https://discordapp.com/invite/fF5KZsw>)")

        await client.send_message(message.channel, embed=embed)     
    elif message.content.startswith('!server-status'):
        embed = discord.Embed(title="Pes6stars bot", description="Status of PES6Stars server.", color=0xeee657)
    
        # give info about you here
        embed.add_field(name="Author", value="Bob")
        close = sock.close()
        sock.close()        
        if result == 0:
           embed.add_field(name="STATUS", value="ONLINE")
           print ("Port is open")
        else:
           embed.add_field(name="STATUS", value="OFFLINE")            
           print ("Port is not open")
        await client.send_message(message.channel, embed=embed)
        

client.run('NDQ2NzYyNTAyOTQ1MTEyMDc1.Dd9vrA.JJH1dpg-64cIdQby0uzfZryhpaU')
