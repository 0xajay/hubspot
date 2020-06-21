import requests
import json

endpoint = 'https://api.hubapi.com/contacts/v1/contact/?hapikey=0b4ad834-3b8a-4ec1-b1fa-e5c418d76734'
headers = {}
headers["Content-Type"]="application/json"


def post_contact(req):

    property = ["email", "firstname", "lastname", "company", "website", "phone", "address", "city","state", "zip"]
    data = {"properties":[]}
    for i in property:
        temp = {}
        temp["property"] = i
        temp["value"] = req[i]
        data["properties"].append(temp)
    data = json.dumps(data)


    r = requests.post( url = endpoint, data = data, headers = headers )

    return True
