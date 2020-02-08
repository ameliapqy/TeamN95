#write user object into JSON string to process & display on website
import json
from user import *

currUser = User()
print(currUser.type)
dict = {
    "uid": currUser.uid,
    "type": currUser.type,
    "name": currUser.name,
    "supplyType": currUser.supplyType,
    "supplyNumber": currUser.supplyNumber,
    "addr": currUser.addr,
    "tel": currUser.tel,
    "email": currUser.email,
    "info": currUser.info
}
userString = json.dumps(dict)
print(userString)


