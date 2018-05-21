import discord
import asyncio
import socket
import requests

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Pes6Stars.cf | !server-status'), status=discord.Status("online"))

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
        embed = discord.Embed(title="Pes6stars bot", description="Pes6stars.cf", color=0xeee657)
    
        # give info about you here
        embed.add_field(name="Author", value="Bob")

        # give users a link to invite thsi bot to their server
        embed.add_field(name="Invite others", value="[Invite link](<https://discordapp.com/invite/fF5KZsw>)")

        await client.send_message(message.channel, embed=embed)     
    elif message.content.startswith('!server-status'):
        url = requests.get("http://pes6stars.cf/onlineplayers.html")
        htmltext = url.text
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('pes6stars.cf',20200))   
        sock.close()      
        if result == 0:
           embed = discord.Embed(title="Pes6Stars Bot", description="Status of Pes6Stars server.", color=0x00ff00)
           embed.add_field(name="Author", value="Bob")
           embed.add_field(name="STATUS", value="ONLINE")
           embed.add_field(name="Online PLayers", value="htmltext")
           print ("Port is open")  
           embed.add_field(name="Lobbies Live!", value="[Lobbies List](<https://pes6stars.cf/lobbies.php>)")  
           await client.send_message(message.channel, embed=embed)
        else:
           embed = discord.Embed(title="Pes6Stars Bot", description="Status of Pes6Stars server.", color=0xff0000)
           embed.add_field(name="Author", value="Bob")
           embed.add_field(name="STATUS", value="OFFLINE")
           print ("Port is not open")  
           embed.add_field(name="Lobbies Live!", value="[Lobbies List](<https://pes6stars.cf/lobbies.php>)")  
           await client.send_message(message.channel, embed=embed)
    elif message.content.startswith('!website-status') or message.content.startswith('!forum-status'):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('pes6stars.cf',80))   
        sock.close()      
        if result == 0:
           embed = discord.Embed(title="Pes6Stars Bot", description="Status of Pes6Stars site.", color=0x00ff00)
           embed.add_field(name="Author", value="Bob")
           embed.add_field(name="STATUS", value="ONLINE")
           print ("Port is open")  
           embed.add_field(name="Lobbies Live!", value="[Lobbies List](<https://pes6stars.cf/lobbies.php>)")  
           await client.send_message(message.channel, embed=embed)
        else:
           embed = discord.Embed(title="Pes6Stars Bot", description="Status of Pes6Stars site.", color=0xff0000)
           embed.add_field(name="Author", value="Bob")
           embed.add_field(name="STATUS", value="OFFLINE")
           print ("Port is not open")  
           embed.add_field(name="Lobbies Live!", value="[Lobbies List](<https://pes6stars.cf/lobbies.php>)")  
           await client.send_message(message.channel, embed=embed)   
    elif message.content.startswith('!onlineplayers') or message.content.startswith('!online-players'):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('pes6stars.cf',80))   
        sock.close()      
        if result == 0:
           embed = discord.Embed(title="Pes6Stars Bot", description="Status of Pes6Stars site.", color=0x00ff00)
           embed.add_field(name="Author", value="Bob")
           embed.add_field(name="STATUS", value="ONLINE")
           print ("Port is open")  
           embed.add_field(name="Lobbies Live!", value="[Lobbies List](<https://pes6stars.cf/lobbies.php>)")  
           await client.send_message(message.channel, embed=embed)
        else:
           embed = discord.Embed(title="Pes6Stars Bot", description="Status of Pes6Stars site.", color=0xff0000)
           embed.add_field(name="Author", value="Bob")
           embed.add_field(name="STATUS", value="OFFLINE")
           print ("Port is not open")  
           embed.add_field(name="Lobbies Live!", value="[Lobbies List](<https://pes6stars.cf/lobbies.php>)")  
           await client.send_message(message.channel, embed=embed)              

        

client.run('NDQ2NzYyNTAyOTQ1MTEyMDc1.Dd9vrA.JJH1dpg-64cIdQby0uzfZryhpaU')
