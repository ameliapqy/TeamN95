#write user object into JSON string to process & display on website
import json
import comm.py

user = User()
dict = {
    "id": user.id
    "type":user.type,
    "name": user.name,
    "supplyType": user.supplyType,
    "supplyNumber": user.supplyNumber,
    "addr": user.addr,
    "tel": user.tel,
    "email": user.email,
    "info": user.info
}
    userString = json.dumps(dict)
    print(userString)


