#read JSON string into object to store into database
import json
import comm.py

#get json string from front end, sample string placeholder for now.
var jsonString = '''{
    		"type": "donor"
            "name": "Llama",
            "supplyType": "mask",
    		"supplyNumber": 1,
    		"addr": "3411 Chestnut st",
    		"tel": "6786467287",
    		"email": "pqy@seas.upenn.edu",
    		"info": "Hi! I'm manufacturing N95 mask please contact me through tel/email if needed"
    }'''


json.loads(dict, jsonString)

#parse dict into User objects
    currUser = User(dict[type], dict[supplyNumber], dict[supplyType], dict[addr], dict[tel], dict[email],dict[info])

#user into database
