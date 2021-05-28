import discord
import view as v
from datetime import datetime
import time
client = discord.Client()
channels = ["macacobot"]
@client.event

async def on_message(message):

    id = client.get_guild(668413162739204106)
    #print(message.channel,message.author,message.content) # Now every message sent will be printed to the console
    if(str(message.author) == 'Macaco#8276' and message.content.find("!spam") != -1):
    	await message.delete()
    	data = str(message.content[6:])    	
    	i = data.index(' ')
    	count = data[:i]
    	msg = data[i+2:-1]
    	print(count,msg)
    	for x in range(int(count)):
    		await message.channel.send(str(msg))
    if(str(message.author) == 'Macaco#8276' and message.content.find("!MacacoMusica") != -1):
    	audio_source = discord.FFmpegPCMAudio('musica.mp3')
    	voice_channel = message.author.voice.channel
    	channel = None
    	if (voice_channel != None):
        	channel = voice_channel.name
        	vc = await voice_channel.connect()
        	vc.play(audio_source)
        	while vc.is_playing():
        		time.sleep(.1)
        	await vc.disconnect()
    	
 #  Check if in correct channel
    if (str(message.channel) in channels and str(message.author) != 'MacacoBOT#2350' ):
    	if message.content.find("!ajuda") != -1:
    		await message.channel.send("!ajuda,!utc,#?,!mortes,!preco")
    	if message.content.find("!utc") != -1:
    		resp = datetime.utcnow().ctime().split(' ')[3]
    		await message.channel.send(resp)
    	if message.content.find("#?") != -1:
    		bo , resp = v.whois(message.content)
    		if(bo):
    			print(resp)
    			embedVar = discord.Embed(color=0x00ff00)
    			for n in range(len(resp['Id'])):
    				
    				embedVar.add_field(name='[' + str(resp['AllianceName'][n]) + ']' +  ' (' + str(resp['GuildName'][n]) + ') ' + str(resp['Name'][n]), value= 'KillFame : ' + str(resp['KillFame'][n]) + ', K/D : ' + str(resp['FameRatio'][n])  , inline=True)
    			await message.channel.send(embed=embedVar)
    		else:
    			await message.channel.send('error')
    		

    	if message.content.find("!mortes") != -1:
    		msg = message.content[8:]
    		print(msg)
    		bol , data = v.deaths(msg)
    		if(bol):
	    		for n in range(len(data['event-id'])):
	    			embedVar = discord.Embed(color=0xff0000,title='Death report',description= 'time : ' + data['event-time'][n] + ', assists : '+data['event-assists'][n], url = 'https://albiononline.com/pt/killboard/kill/' + data['event-id'][n] )
	    			embedVar.add_field(name = 'Killer' , value = data['killer-nick'][n] , inline = True)
	    			embedVar.add_field(name = '------>' , value = '------>' , inline = True)
	    			embedVar.add_field(name = 'Victim ' , value = data['victim-nick'][n] , inline = True)
	    			embedVar.add_field(name = 'Ip ' , value = data['killer-ip'][n] , inline = True)
	    			embedVar.add_field(name = '------>' , value = '------>' , inline = True)
	    			embedVar.add_field(name = 'Ip' , value = data['victim-ip'][n] , inline = True)
	    			embedVar.add_field(name = 'HeadHoldreport' , value ='https://handholdreport.com/killboard/'+  str(data['event-battleid'][n]) , inline = True)
	    			await message.channel.send(embed=embedVar)
    		else:
    			await message.channel.send("error")


    	if message.content.find("!preco") != -1:
    		if(message.content.find('.')!= -1):
    			pos = message.content.index('.')
    			msg = message.content[7:pos-2]
	    		tier = message.content[pos-1:pos]
	    		enc = message.content[pos+1:pos+2]
	    	else:
	    		msg = message.content[7:]
	    		tier = -1
	    		enc = -1
    		
	    	print(msg,tier,enc)	
    		bo , resp = v.price(msg,tier,enc)
    		if(bo):
	    		resp = resp.sort_values(by='sell_price_min').reset_index(drop=True)
	    		embedVar = discord.Embed(color=0xff0000)
	    		for n in range(len(resp['sell_price_min'])):
	    			embedVar.add_field(name = resp['sell_price_min_date'][n] , value = resp['city'][n] + ' : ' + str(resp['sell_price_min'][n]) + '\n' + 'quality : ' + str(resp['quality'][n]) )
	    		await message.channel.send(embed=embedVar)
	    	else:
	    		await message.channel.send('error')
		

client.run("NzU5Mjk5MDI3NjM2MDYwMTkw.X27eUw.jyqBfpW4INvqUu61NbSmy3cQVJM")