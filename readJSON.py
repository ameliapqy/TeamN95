#read JSON string into object to store into database
import json
from user import *

def JSONToObject(jsonString):
    dict = json.loads(jsonString)
    currUser = User()
    currUser.setAll(dict['type'], dict['name'], dict['supplyType'], dict['supplyNumber'], dict['addr'], dict['tel'], dict['email'],dict['info'])
    
    return currUser


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


def test():
    #parse dict into User objects
    user = JSONToObject(jsonString)
    user.name = "Llama"
    user.intro()
    #user into database

def testPrompt():
    #parse dict into User objects
    user = JSONToObject(jsonString)
    user.name = "Llama"
    user.intro()
    #user into database
test()