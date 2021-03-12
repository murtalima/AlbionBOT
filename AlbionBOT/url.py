import requests
import pandas as pd

def pegar_dados(site):
    kills=[]
    r = requests.get(site)
    print(r)
    data = r.json()

    df = pd.DataFrame(data)
    for x in data:
        kill = {'numberOfParticipants': [],
                'EventId': [],
                'TimeStamp': [],
                'AverageItemPower': [],
                'Name': [],
                'GuildName': [],
                'AllianceName': [],
                'MyAverageItemPower': [],
                'Equipment': [],
                'DeathFame':x['TotalVictimKillFame']
                }
        if(x['numberOfParticipants'] >= 0):
            kill['numberOfParticipants'].append(x['numberOfParticipants'])
        else:
            kill['numberOfParticipants'].append(-1)
        kill['EventId'].append("https://albiononline.com/pt/killboard/kill/"+str(x['EventId']))
        kill['TimeStamp'].append(x['TimeStamp'][5:13])
        kill['AverageItemPower'].append(x['Killer']['AverageItemPower'])
        kill['Name'].append(x['Killer']['Name'])
        kill['GuildName'].append(x['Killer']['GuildName'])
        kill['AllianceName'].append(x['Killer']['AllianceName'])
        kill['MyAverageItemPower'].append(x['Victim']['AverageItemPower'])
        try:
            arma = x['Victim']['Equipment']['MainHand']['Type']
        except:
            arma = "Sem arma"
        try:
            capacete=x['Victim']['Equipment']['Head']['Type']
        except:
            capacete = "Sem capacete"
        try:
            peito=x['Victim']['Equipment']['Armor']['Type']
        except:
            peito="Sem peito"
        try:
            bota=x['Victim']['Equipment']['Shoes']['Type']
        except:
            bota="Sem bota"
        try:
            capa=x['Victim']['Equipment']['Cape']['Type']
        except:
            capa = "Sem capa"
        kill['Equipment'].append(arma)
        kill['Equipment'].append(capacete)
        kill['Equipment'].append(peito)
        kill['Equipment'].append(bota)
        kill['Equipment'].append(capa)
        kills.append(kill)

    print(kills)
    return kills[0:3]