import requests
from urllib.parse import urlencode
api_key="306cf1684a42e4be5ec0a1c60362c2ef"

def extreact_data(value,data_type='platforms'):    
    endpoint = f"https://libraries.io/api/{data_type}"
# search?q=grunt&
    
    params={"q":{value},"api_key":api_key}    
    url_parmas=urlencode(params)
    url= f"{endpoint}?{url_parmas}"
    r=requests.get(url).json()
    
    
   
    return r
   

