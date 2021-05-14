import requests
from urllib.parse import urlencode

import os
api_url = os.getenv("api_url")
import json

# scheme='https',
# netloc='https://libraries.io',

class url:
    def __init__(self,api_url):
        self.url=api_url

    def end(self):
        u= self.url

        return u
        

params='',
query='api_key=YOUR_API_KEY', 
fragment=''

# api_key="306cf1684a42e4be5ec0a1c60362c2ef"


class api_endpoint():
    def base_url(path,query):
        url=f"{api_url}{path}?{query}"
        dum_data=requests.get(url)
        json_fiter=dum_data.json()        
        response =json.dumps(json_fiter)  
        responses =json.loads(response)  
        return responses

        
    def url(path):
        url=f"{api_url}{path}?{api_url}"
        dum_data=requests.get(url)
        json_fiter=dum_data.json()        
        response =json.dumps(json_fiter)  
        responses =json.loads(response)  



        return responses    
        # print(url)
# 

