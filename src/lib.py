import pandas as pd
import requests
def whois_data (data):
	df = pd.DataFrame(data['players'])
	return df[['Id','AllianceName','GuildName','Name','KillFame','DeathFame','FameRatio']]
def deaths_data (data):
	df = {
		'victim-nick':[],
		'victim-ip':[],
		'victim-bag':[],
		'victim-helmet':[],
		'victim-cape':[],
		'victim-weapon':[],
		'victim-offhand':[],
		'victim-food':[],
		'victim-potion':[],
		'victim-mount':[],
		'victim-inventory':[],
		'killer-nick':[],
		'killer-ip':[],
		'killer-bag':[],
		'killer-helmet':[],
		'killer-cape':[],
		'killer-weapon':[],
		'killer-offhand':[],
		'killer-food':[],
		'killer-potion':[],
		'killer-mount':[],
		'killer-inventory':[],
		'event-time':[],
		'event-id':[],
		'event-assists':[],
		'event-battleid':[]

	}
	print(len(data))

	for event in data:
		
		vname = str(event['Victim']['Name'])
		vip = str(event['Victim']['AverageItemPower'])
		if(event['Victim']['Equipment']['Bag'] != None):
			vbag = str(event['Victim']['Equipment']['Bag']['Type'])
		else:
			vbag = 'None'
		if(event['Victim']['Equipment']['Head'] != None):
			vhelmet = str(event['Victim']['Equipment']['Head']['Type'])
		else:
			vhelmet = 'None'
		if(event['Victim']['Equipment']['Cape'] != None):
			vcape = str(event['Victim']['Equipment']['Cape']['Type'])
		else:
			vcape = 'None'
		if(event['Victim']['Equipment']['MainHand'] != None):
			vweapon = str(event['Victim']['Equipment']['MainHand']['Type'])
		else:
			vweapon = 'None'
		if(event['Victim']['Equipment']['OffHand'] != None):
			voffhand = str(event['Victim']['Equipment']['OffHand']['Type'])
		else:
			voffhand = 'None'
		if(event['Victim']['Equipment']['Food'] != None):
			vfood = str(event['Victim']['Equipment']['Food']['Type'])
		else:
			vfood = 'None'
		if(event['Victim']['Equipment']['Potion'] != None):
			vpot = str(event['Victim']['Equipment']['Potion']['Type'])
		else:
			vpot = 'None'
		if(event['Victim']['Equipment']['Mount'] != None):
			vmount = str(event['Victim']['Equipment']['Mount']['Type'])
		else:
			vmount = 'None'
		if(event['Victim']['Inventory'] != None):
			inv = event['Victim']['Inventory']
			vinv = {
				'Type' :[],
				'Count' :[]
			}
			for item in inv:
				if (item != None):
					vinv['Type'].append(item['Type'])
					vinv['Count'].append(item['Count'])
		else:
			vinv = 'None'

		kname = str(event['Killer']['Name'])
		kip = str(event['Killer']['AverageItemPower'])
		if(event['Killer']['Equipment']['Bag'] != None):
			kbag = str(event['Killer']['Equipment']['Bag']['Type'])
		else:
			kbag = 'None'
		if(event['Killer']['Equipment']['Head'] != None):
			khelmet = str(event['Killer']['Equipment']['Head']['Type'])
		else:
			khelmet = 'None'
		if(event['Killer']['Equipment']['Cape'] != None):
			kcape = str(event['Killer']['Equipment']['Cape']['Type'])
		else:
			kcape = 'None'
		if(event['Killer']['Equipment']['MainHand'] != None):
			kweapon = str(event['Killer']['Equipment']['MainHand']['Type'])
		else:
			kweapon = 'None'
		if(event['Killer']['Equipment']['OffHand'] != None):
			koffhand = str(event['Killer']['Equipment']['OffHand']['Type'])
		else:
			koffhand = 'None'
		if(event['Killer']['Equipment']['Food'] != None):
			kfood = str(event['Killer']['Equipment']['Food']['Type'])
		else:
			kfood = 'None'
		if(event['Killer']['Equipment']['Potion'] != None):
			kpot = str(event['Killer']['Equipment']['Potion']['Type'])
		else:
			kpot = 'None'
		if(event['Killer']['Equipment']['Mount'] != None):
			kmount = str(event['Killer']['Equipment']['Mount']['Type'])
		else:
			kmount = 'None'
		if(event['Killer']['Inventory'] != None):
			inv = event['Killer']['Inventory']
			kinv = {
				'Type' :[],
				'Count' :[]
			}
			for item in inv:
				if (item != None):
					vinv['Type'].append(item['Type'])
					vinv['Count'].append(item['Count'])
		else:
			kinv = 'None'
		df['victim-nick'].append(vname)
		df['victim-ip'].append(vip)
		df['victim-bag'].append(vbag)
		df['victim-helmet'].append(vhelmet)
		df['victim-cape'].append(vcape)
		df['victim-weapon'].append(vweapon)
		df['victim-offhand'].append(voffhand)
		df['victim-food'].append(vfood)
		df['victim-potion'].append(vpot)
		df['victim-mount'].append(vmount)
		df['victim-inventory'].append(vinv)

		df['killer-nick'].append(kname)
		df['killer-ip'].append(kip)
		df['killer-bag'].append(kbag)
		df['killer-helmet'].append(khelmet)
		df['killer-cape'].append(kcape)
		df['killer-weapon'].append(kweapon)
		df['killer-offhand'].append(koffhand)
		df['killer-food'].append(kfood)
		df['killer-potion'].append(kpot)
		df['killer-mount'].append(kmount)
		df['killer-inventory'].append(kinv)
		
		df['event-time'].append(str(event['TimeStamp'][:-11]))
		df['event-id'].append(str(event['EventId']))
		df['event-assists'].append(str(event['numberOfParticipants']))
		df['event-battleid'].append(str(event['BattleId']))

	df = pd.DataFrame(df)
	return df
def price_data (item):
	resp = []
	col_names = ['x', 'data_name', 'game_name']
	dicionario = pd.read_csv('items.csv', names=col_names, delimiter=':', error_bad_lines=False,skipinitialspace=True)
	for x in range(len(dicionario['game_name'])):
		if str(item).lower() in str(dicionario['game_name'][x]).lower():
			resp.append(dicionario['data_name'][x].replace(' ',''))
	return resp
def price_df (df):
	for x in df:
		ndf = pd.DataFrame(x)
		ndf =ndf[['city' , 'quality','sell_price_min', 'sell_price_min_date']][ndf.sell_price_min != 0]
	return ndf
