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
    elif message.content.startswith('!clear823'):
        tmp = await client.send_message(message.channel, 'Clearing messages...')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!verifyhelp') or message.content.startswith('!verify-help') or message.content.startswith('!getverified'):
        await client.send_message(message.channel, "```First: You need to open the PES6 game and type at the chat at any place at game @verifyme```")  
        await client.send_message(message.channel, "```Second: Go to #verificaton channel and type !verify [profile name], The profile name which you are logged with it and type with it @verifyme command!```")       
    elif message.content.startswith('!verify') or message.content.startswith('!Verify') or message.content.startswith('!VERIFY'):
           msg = message.content.strip()
           profilename = msg[7:].strip()
           print (profilename)
           url = requests.get("http://80.211.157.169/adminususus/verify.php?p=statsdiscordbot125&profile=%s" % profilename)
           htmltext = url.text
           print (htmltext)
           if htmltext == "1":       
               await client.change_nickname(message.author, profilename)
               verifiedrole = discord.utils.get(message.server.roles, name="Verified Player")
               nonverifiedrole = discord.utils.get(message.server.roles, name="Non-Verified Player")
               await asyncio.sleep(2)
               await client.add_roles(message.author, verifiedrole)
               await asyncio.sleep(2)
               await client.remove_roles(message.author, nonverifiedrole)
               await client.send_message(message.author, "```"+"You are now verified "+profilename+"```")
               await client.send_message(client.get_channel('440854555010400266'), ""+profilename+" has been verified.")
               await client.delete_message(message)
           else:
                await asyncio.sleep(2)
                await client.delete_message(message)
                await client.send_message(message.channel, "```Their is a problem on your verification, Type @verifyme command again at PES6 game firstly.```")                
    elif message.content.startswith('!status') or message.content.startswith('!STATUS') or message.content.startswith('!Status'):
        embed = discord.Embed(title="Pes6stars bot", description="Pes6stars.cf", color=0xeee657)
    
        # give info about you here
        embed.add_field(name="Author", value="Bob")

        # give users a link to invite thsi bot to their server
        embed.add_field(name="Invite others!", value="[Invite link](<https://discordapp.com/invite/fF5KZsw>)")

        await client.send_message(message.channel, embed=embed)     
    elif message.content.startswith('!server-status') or message.content.startswith('!SERVER-STATUS') or message.content.startswith('!Server-Status'):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('80.211.157.169',20200))   
        sock.close()      
        if result == 0:
           url = requests.get("http://80.211.157.169/onlineplayers.php")
           htmltext = url.text
           embed = discord.Embed(title="Pes6Stars Bot", description="Status of Pes6Stars server.", color=0x00ff00)
           embed.add_field(name="Lobbies Live!", value="[Lobbies List](<https://pes6stars.cf/lobbies.php>)")
           embed.add_field(name="STATUS", value="ONLINE")
           embed.add_field(name="Online Players", value=htmltext)
           print ("Port is open")  
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
    elif message.content.startswith('!onlineplayers') or message.content.startswith('!online-players') or message.content.startswith('!online-users') or message.content.startswith('!usersonline') or message.content.startswith('!onlineusers'):
           url = requests.get("http://80.211.157.169/onlineplayers.php")
           htmltext = url.text
           embed = discord.Embed(title="Pes6Stars Bot", description="Online players at Pes6stars server now.", color=0x00ff00)
           embed.add_field(name="Online Players", value=htmltext)
           await client.send_message(message.channel, embed=embed)  
    elif message.content.strip().startswith('!stats') or message.content.startswith('!STATS') or message.content.startswith('!Stats'):
           msg = message.content.strip()
           profilename = msg[6:].strip()
           print (profilename)
           url = requests.get("http://80.211.157.169/adminususus/stats.php?p=statsdiscordbot125&profile=%s" % profilename)
           htmltext = url.text
           embed = discord.Embed(title="Pes6Stars Bot", description="Stats of your profile.", color=0x00ff00)
           embed.add_field(name="Stats", value=htmltext)
           await client.send_message(message.channel, embed=embed)           
    elif message.content.strip().startswith('!top1') or message.content.startswith('!TOP1') or message.content.startswith('!Top1'):
           url = requests.get("http://80.211.157.169/adminususus/stats.php?p=statsdiscordbot125&top1=list")
           htmltext = url.text
           embed = discord.Embed(title="Pes6Stars Bot", description="Top player rank #1 in Pes6Stars Server.", color=0x00ff00)
           embed.add_field(name="Top Player", value=htmltext)
           await client.send_message(message.channel, embed=embed)         

        

client.run('NDQ2NzYyNTAyOTQ1MTEyMDc1.Dd9vrA.JJH1dpg-64cIdQby0uzfZryhpaU')
