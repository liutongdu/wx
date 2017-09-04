#by liutong 
#licenced through GPL
#you can use it totally for free
#contact me by liutongdu@bupt

import requests

url = 'http://10.3.8.211/'
log_data = { 'DDDDD': '**your account', 'upass': '**your password','0MKKey': ''}
session = requests.Session()
req = session.post(url, data = log_data)
print('success')