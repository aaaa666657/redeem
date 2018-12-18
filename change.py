# -*- coding: utf-8 -*-
import os.path

from flask import Flask,send_file,request
import pymongo



app = Flask(__name__, static_url_path='')


myclient = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = myclient.list_database_names()
DB = myclient.isweek2018.gifts
######################################################king

@app.route('/know/read', methods=['GET', 'POST']) 
def know_read():
	if request.method == 'POST': 
		res = DB.find_one({'type':'king',"username" : request.values['username']})       	
		if res:
			if res["redeemed"]:
				return "已兌換過獎品"
			else:
				return "可兌換獎品"
		else:
 			return "未參加活動"

	return "<form method='post' action='/know/read'><input type='text' name='username' /></br><button type='submit'>Submit</button></form>"

@app.route('/know/write', methods=['GET', 'POST']) 
def know_write():
	if request.method == 'POST': 
		res = DB.find_one({'type':'king',"username" : request.values['username']})       	
		
		if res:
			if res["redeemed"]:
				return "已兌換過獎品"
			else:
				temp2 = res.copy()
				temp["redeemed"] = True
				DB.save(temp)
				return "可兌換獎品"
		else:
 			return "未參加活動"

	return "<form method='post' action='/know/write'><input type='text' name='username' /></br><button type='submit'>Submit</button></form>"
######################################################RPG
@app.route('/rpg/read', methods=['GET', 'POST']) 
def rpg_read():
	if request.method == 'POST': 
		res = DB.find_one({'type':'RPG',"username" : request.values['username']})       	
		if res:
			if res["redeemed"]:
				return "已兌換過獎品"
			else:
				return "可兌換獎品"
		else:
 			return "未參加活動"

	return "<form method='post' action='/rpg/read'><input type='text' name='username' /></br><button type='submit'>Submit</button></form>"

@app.route('/rpg/write', methods=['GET', 'POST']) 
def rpg_write():
	if request.method == 'POST': 
		res = DB.find_one({'type':'RPG',"username" : request.values['username']})       	
		
		if res:
			if res["redeemed"]:
				return "已兌換過獎品"
			else:
				temp2 = res.copy()
				temp["redeemed"] = True
				DB.save(res)
				return "可兌換獎品"
		else:
 			return "未參加活動"

	return "<form method='post' action='/rpg/write'><input type='text' name='username' /></br><button type='submit'>Submit</button></form>"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0') 
				
