import discord
import url as u
import requests
from datetime import datetime
import pandas as pd
from tabulate import tabulate
import winsound
import io
import cv2
import numpy as np
import time
frequency = 1000  # Set Frequency To 2500 Hertz
duration = 2000  # Set Duration To 1000 ms == 1 second
from time import gmtime
#id 668413162739204106
client = discord.Client()
aprovados = []
sets_novos = []
perm =[]
perm.append('MacacoLima#6373')
perm.append('AmebaMedonha#2466')
perm.append('Zeylon#8122')
perm.append('RatoSujo (Zukah)#9823')
channels = ["macacobot"]
healer=['MAIN_HOLYSTAFF','2H_HOLYSTAFF','2H_DIVINESTAFF','MAIN_HOLYSTAFF_MORGANA','2H_HOLYSTAFF_HELL','2H_HOLYSTAFF_UNDEAD' , 'MAIN_HOLYSTAFF_AVALON']
@client.event

async def on_message(message):

    id = client.get_guild(668413162739204106)

    #print(message.channel,message.author,message.content) # Now every message sent will be printed to the console
  # Check if in correct channel
    if (str(message.author) in perm or str(message.channel) in channels):
        if message.content.find("!ba#1") != -1:

            url = "https://render.albiononline.com/v1/guild/logo.png?schema=SCHEMA_01&primarySchemaColor=1&secondarySchemaColor=12&symbol=Nilfgaard&size=200&symbolColor=2&type=ACTIVE_GUILD_CRYSTAL_LEADER&symbolScale=0.85&symbolOffsetY=0.1&gems=4"
            r = requests.get(url)
            data = io.BytesIO(r.content)
            await message.channel.send(file=discord.File(data, 'cool_image.png'))
        if message.content.find("!img") != -1:
            cc = 0
            col_names = ['x', 'data_name', 'game_name']
            dicionario = pd.read_csv('items.csv', names=col_names, delimiter=':', error_bad_lines=False,
                                     skipinitialspace=True)
            item = message.content[5:]
            #print(item)
            encontrado = False
            for x in range(len(dicionario['game_name'])):
                if str(item).lower() in str(dicionario['game_name'][x]).lower():
                    encontrado = True
                    cc += 1
                    if cc < 2:
                        try:
                            url2 = 'https://render.albiononline.com/v1/item/' + dicionario['data_name'][x] + "?size=200"
                            url2 = url2.replace(' ', '')
                            #print(url2)
                            r = requests.get(url2)
                            data = io.BytesIO(r.content)
                            await message.channel.send(file=discord.File(data, 'cool_image.png'))
                        except:
                            pass
            if(encontrado!=True):
                await message.channel.send("nao encontrado")

        if message.content.find("!preco") != -1:
            cc=0
            col_names = ['x', 'data_name', 'game_name']
            dicionario = pd.read_csv('items.csv', names=col_names, delimiter=':', error_bad_lines=False,
                                      skipinitialspace=True)
            item = message.content[7:]
            #print(item)

            for x in range(len(dicionario['game_name'])):
                if str(item).lower() in str(dicionario['game_name'][x]).lower():
                    cc += 1
                    if cc < 8:

                        await message.channel.send(dicionario['data_name'][x])

                        url_ = "https://www.albion-online-data.com/api/v2/stats/prices/"+dicionario['data_name'][x]+"?locations=Caerleon, Bridgewatch,Fort Sterling,Lymhurst,Martlock,Thetford"
                        r=0
                        r = requests.get(url_)
                        data = r.json()
                        df=pd.DataFrame(data)
                        try:
                            url2 = 'https://render.albiononline.com/v1/item/' + dicionario['data_name'][x] + "?size=100"
                            url2 = url2.replace(' ','')
                            #print(url2)
                            r = requests.get(url2)
                            data = io.BytesIO(r.content)
                        except:
                            data = []
                        index = df[df['sell_price_min'] == 0].index
                        df.drop(index, inplace=True)
                        await message.channel.send(
                            df[['quality', 'city', 'sell_price_min']].sort_values(by='sell_price_min').to_string(
                                index=False), file=discord.File(data, 'cool_image.png'))
        if message.content.find("!preço") != -1:
            dicionario = pd.read_csv("yoink.csv")
            ct = True
            try:
                tier = int(message.content[7:8])
                encantamento = int(message.content[9:10])
            except:
                tier = -1
                encantamento = -1
            if (9>tier>0 and 4>encantamento>-1):

                if(encantamento!=0):
                    #print(encantamento)
                    encantamento = '@' + str(encantamento)
                else:
                    encantamento =''
                item = (message.content[11:]).lower()
                achou = False
                for x in range(len(dicionario['game_name'])):
                    if item  == dicionario['game_name'][x]:
                        achou = True
                        await message.channel.send(dicionario['data_name'][x])
                        url_ = "https://www.albion-online-data.com/api/v2/stats/prices/T" + str(tier)+"_"+dicionario['data_name'][x]+encantamento+"?locations=Caerleon, Bridgewatch,Fort Sterling,Lymhurst,Martlock,Thetford"
                        r = requests.get(url_)
                        if (r.status_code == 200):
                            data = r.json()
                            pd.option_context('display.max_columns', None)
                            df = pd.DataFrame(data)
                            index = df[df['sell_price_min_date']=='0001-01-01T00:00:00'].index
                            df.drop(index,inplace=True)
                            #print(df[['city','sell_price_min']])
                            url2 = 'https://render.albiononline.com/v1/item/T'+str(tier)+'_'+ dicionario['data_name'][x]+encantamento+"?size=100"
                            #print(url2)
                            r = requests.get(url2)
                            data = io.BytesIO(r.content)
                            await  message.channel.send(file=discord.File(data, 'cool_image.png'))
                            await message.channel.send(df[['quality' ,'city','sell_price_min']].sort_values(by='sell_price_min').to_string(index=False))

        if message.content.find("!MacacoLima") != -1:
            tempo = gmtime()
            print(str(tempo))
            print(message.author)
            winsound.Beep(frequency, duration)
        if message.content.find("!ajuda") != -1:
            await message.channel.send ("!pedras, !metal, !pano , !utc , !mortes <nick> e ?<nick>")
        if message.content.find("!pedras") != -1:
            df=[]

            for x in range(5):
                r = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T" + str(x + 4) + "_STONEBLOCK?locations=Bridgewatch,Fort Sterling,Lymhurst,Martlock,Thetford")
                if (r.status_code == 200):
                    data = r.json()
                    new_row = {'Tier':str(x+4),'Bridgewatch': data[0]['sell_price_min'], 'Fort Sterling': data[1]['sell_price_min'],
                               'Lymhurst': data[2]['sell_price_min'], 'Martlock': data[3]['sell_price_min'],
                               'Thetford': data[4]['sell_price_min']}
                    #print(new_row)
                    df.append(new_row)
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            df = pd.DataFrame(df)
            await message.channel.send(df.to_string(index = False))
        if message.content.find("!metal") != -1:
            df=[]

            for x in range(5):
                r = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T" + str(x + 4) + "_METALBAR?locations=Bridgewatch,Fort Sterling,Lymhurst,Martlock,Thetford")
                if (r.status_code == 200):
                    data = r.json()
                    new_row = {'Tier':str(x+4),'Bridgewatch': data[0]['sell_price_min'], 'Fort Sterling': data[1]['sell_price_min'],
                               'Lymhurst': data[2]['sell_price_min'], 'Martlock': data[3]['sell_price_min'],
                               'Thetford': data[4]['sell_price_min']}
                    #print(new_row)
                    df.append(new_row)
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            df = pd.DataFrame(df)
            await message.channel.send(df.to_string(index = False))
        if message.content.find("!pano") != -1:
            df=[]

            for x in range(5):
                r = requests.get("https://www.albion-online-data.com/api/v2/stats/prices/T" + str(x + 4) + "_CLOTH?locations=Bridgewatch,Fort Sterling,Lymhurst,Martlock,Thetford")
                if (r.status_code == 200):
                    data = r.json()
                    new_row = {'Tier':str(x+4),'Bridgewatch': data[0]['sell_price_min'], 'Fort Sterling': data[1]['sell_price_min'],
                               'Lymhurst': data[2]['sell_price_min'], 'Martlock': data[3]['sell_price_min'],
                               'Thetford': data[4]['sell_price_min']}
                    #print(new_row)
                    df.append(new_row)
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            df = pd.DataFrame(df)
            await message.channel.send(df.to_string(index = False))
        if message.content.find("!utc") != -1:
            await message.channel.send(datetime.utcnow())
        if message.content.find("!mortes") != -1:
            msg = ""
            Nome = message.content[8:]
            print(Nome)
            r = requests.get("https://gameinfo.albiononline.com/api/gameinfo/search?q=" + Nome)
            print(r.status_code)
            if (r.status_code == 200):
                data = r.json()
            Nome = data['players'][0]['Id']
            print(Nome)
            site = "https://gameinfo.albiononline.com/api/gameinfo/players/"+Nome+"/deaths"
            print(site)
            kill = u.pegar_dados(site)
            kill = pd.DataFrame(kill)
            print(kill)
            print(len(kill))



            for x in range(len(kill['EventId'])):
                print(x)
                event = kill['EventId'][x][0]
                time = kill['TimeStamp'][x][0]
                num = kill['numberOfParticipants'][x][0]
                ip = kill['AverageItemPower'][x][0]
                name = kill['Name'][x][0]
                guild = kill['GuildName'][x][0]
                ally = kill['AllianceName'][x][0]
                myip = kill['MyAverageItemPower'][x][0]
                equip = kill['Equipment'][x]
                print(event,time,num,ip,name,guild)
                embedVar = discord.Embed(title="Morte", description=event, color=0x00ff00, )
                embedVar.add_field(name="hora", value=time, inline=True)
                embedVar.add_field(name="nome", value=name, inline=True)
                if(len(guild) <= 2):
                    guild = [" "]
                embedVar.add_field(name="guild", value=guild, inline=True)
                if (len(ally) <= 2):
                    ally = [" "]
                embedVar.add_field(name="ally", value=ally, inline=True)
                embedVar.add_field(name="num", value=num, inline=True)
                embedVar.add_field(name="ip", value=ip, inline=True)
                embedVar.add_field(name="ip da vitima", value=myip, inline=True)
                embedVar.add_field(name="fama dropada", value=kill['DeathFame'][x], inline=True)
                print(equip)
                img = []
                cc = 0
                for y in equip:

                    url2 = 'https://render.albiononline.com/v1/item/' + y + "?size=80"
                    url2 = url2.replace(' ', '')
                    print(url2)
                    r = requests.get(url2, stream=True).raw

                    data = np.asarray(bytearray(r.read()), dtype="uint8")
                    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
                    img.append(data)
                img = cv2.hconcat(img)
                is_success, buffer = cv2.imencode(".jpg", img)
                io_buf = io.BytesIO(buffer)
                file = discord.File(io_buf, 'image.png')
                await message.channel.send(file=file,embed=embedVar)

            #await message.channel.send(kill[['numberOfParticipants','EventId','TimeStamp','AverageItemPower','Name','GuildName','AllianceName','MyAverageItemPower']].to_string(index=False))

        if message.content.find("#?") != -1:
            Nome = message.content[3:]
            print(Nome)
            r = requests.get("https://gameinfo.albiononline.com/api/gameinfo/search?q=" + Nome)
            print(r)
            if (r.status_code == 200):
                data = r.json()
                #print(data)
                #print(len(data['guilds']))
                #print(data['players'])
                pd.set_option("display.max_rows", None, "display.max_columns", None)
                pd.options.display.width = 1
                if(len(data['players']) >0):
                        df = pd.DataFrame(data['players'])
                        await message.channel.send(tabulate(df[['Name','GuildName','AllianceName','KillFame','DeathFame','FameRatio']], tablefmt="plain"))
                if (len(data['guilds']) >0):
                    gdf = pd.DataFrame(data['guilds'])
                    await message.channel.send("Guilds :\n" + tabulate(gdf[['Name','KillFame','AllianceName','DeathFame']],tablefmt="plain"))




client.run("NzU5Mjk5MDI3NjM2MDYwMTkw.X27eUw.J6Us1i3PSmuWJ0z_xqMr3lenbns")

#async with session.get(my_url) as resp:
#        if resp.status != 200:
#            return await channel.send('Could not download file...')
#        data = io.BytesIO(await resp.read())
#        await channel.send(file=discord.File(data, 'cool_image.png'))
#
#
#
#
#