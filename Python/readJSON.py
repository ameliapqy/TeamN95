#read JOSN object into 
import json
import comm.py

#get json string from front end, sample string placeholder for now.
var jsonString = '''{
    "id": "233",
    "name": "Llama",
    "supply": [
        {
            "type": "mask",
            "number": 6
        },
        {
            "type": "medical kit",
            "number": 8
        }
    ]
		"addr": "3411 Chestnut st",
		"tel": "6786467287",
		"email": "pqy@seas.upenn.edu",
		"info": "Hi! I'm manufacturing N95 mask please contact me through tel/email if needed"
        }'''


json.loads(dict, jsonString)

#parse dict into seeker & supplier objects
if(dict[type]):
    currUser = Seeker(dict[id], dict[supply], dict[addr], dict[tel], dict[email],dict[info])
else: 
    currUser = Donner(dict[id], dict[supply], dict[addr], dict[tel], dict[email],dict[info])

