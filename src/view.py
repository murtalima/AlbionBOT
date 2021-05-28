import discord
import requests
import lib
def whois (msg):
	Nome = msg[3:]
	print(Nome)
	r = requests.get("https://gameinfo.albiononline.com/api/gameinfo/search?q=" + Nome)
	print(r)
	if (r.status_code == 200):
	    data = r.json()
	    data = lib.whois_data(data)
	    return True , data
	else:
		return False , "error"
def get_id_by_name(Name):
	site = "https://gameinfo.albiononline.com/api/gameinfo/search?q=" + Name
	print(site)
	r = requests.get(site)
	print(r.status_code)
	if (r.status_code == 200):
		data = r.json()
		print(len(data['players']))
		if(len(data['players'])>0):
			Id = data['players'][0]['Id']
			return True , Id
	else:
		return False , "error"
	return False , "error"
def deaths (Name):
	bol , id = get_id_by_name(Name)
	if(bol != False):
		site = "https://gameinfo.albiononline.com/api/gameinfo/players/"+str(id)+"/deaths"
		print(site)
		r = requests.get(site)
		print(r.status_code)
		if(r.status_code ==200):
			data = r.json()
			df = lib.deaths_data(data)
			return True , df
		else:
			return False , "error"
	return False , "error"
			
def get_img (item_name):
	site = 'https://render.albiononline.com/v1/item/' + str(item_name) + "?size=200"
	print(site)
	r = requests.get(site)
	print(r.status_code)
	if(r.status_code == 200):
		return True , io.BytesIO(r.content)
	else:
		return False ,'error'
def price (item,tier,enc):
	data = lib.price_data(item)
	df = []
	if(len(data)>0):
		if (tier != -1):
			data = [i for i in data if tier in i]
			print(data[0])
			if(int(enc) == 0):
				data = [data[0]]
			else:
				data = [i for i in data if enc in i[-2:]]
			for x in data:
				site ="https://www.albion-online-data.com/api/v2/stats/prices/"+x
				print(site)
				r = requests.get(site)
				print(r.status_code)
				if(r.status_code == 200):
					df.append(r.json())
				else:
					return False, 'error'
			
			
		else:
			site ="https://www.albion-online-data.com/api/v2/stats/prices/"+data[0]
			print(site)
			r = requests.get(site)
			print(r.status_code)
			if(r.status_code == 200):
				df.append(r.json())
			else:
				return False, 'error'

		df = lib.price_df(df)
		return True , df
	else:
		return False, 'error'