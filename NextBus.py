#William Rickert
#Next Bus parser - check the nextbus service and finds when the next two are
#info from - https://gist.github.com/grantland/7cf4097dd9cdf0dfed14

import requests
import json

resp = requests.get('http://webservices.nextbus.com/service/publicJSONFeed?command=predictions&a=cyride&r=3S&s=1045')

data = resp.json()


#This works if there is only one prediction
#print(data['predictions']['direction']['prediction']['minutes'])

print(data['predictions']['direction']['prediction'][0]['minutes'])
print(data['predictions']['direction']['prediction'][1]['minutes'])
