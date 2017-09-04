import requests

url = 'http://10.3.8.211/F.htm'
session = requests.Session()
req = session.get(url,)

print('logout success!')