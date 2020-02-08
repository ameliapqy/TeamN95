#read JSON string into object to store into database
import json
from user import *

#get json string from front end, sample string placeholder for now.
jsonString = '''{
    		"type": "donor",
            "name": "Llama",
            "supplyType": "mask",
    		"supplyNumber": 1,
    		"addr": "3411 Chestnut st",
    		"tel": "6786467287",
    		"email": "pqy@seas.upenn.edu",
    		"info": "Hi! I'm manufacturing N95 mask please contact me through tel/email if needed"
            }'''

dict = json.loads(jsonString)
#print(dict)
#parse dict into User objects
currUser = User()
currUser.setAll(dict['type'], dict['name'], dict['supplyType'], dict['supplyNumber'], dict['addr'], dict['tel'], dict['email'],dict['info'])
currUser.intro()
#user into database
