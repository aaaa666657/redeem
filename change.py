from flask import Flask, request
import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = myclient.list_database_names()


app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST']) 
def login():
	if request.method == 'POST': 
		res = myclient.test.users.find_one({"username" : request.values['username']})       	
		if res:
			if res["redeemed"]:
				return "already redeemed"
			else:
				temp = myclient.test.users.find_one({"username" : request.values['username'], "redeemed" : False})
				temp2 = temp.copy()
				temp["redeemed"] = True
				myclient.test.users.save(temp)
				return "Can redeem"
		else:
 			return "Not Found"	
		return 'Hello ' + request.values['username'] 

	return "<form method='post' action='/login'><input type='text' name='username' /></br><button type='submit'>Submit</button></form>"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0') 
