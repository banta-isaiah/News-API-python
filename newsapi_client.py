import requests


class client():
    def __init__():

    





def get_top_headlines():
    url = 'https://newsapi.org/v2/top-headlines' 
    
    headers = {
            'X-Api-Key': '34e4c908797d4f99a4b146c973ae314e'}
    params = {'q': None,
              'country': 'us'}
    r = requests.get(url, headers=headers, params=params)
    print(r.request.headers) 
    #print(r.text)


get_top_headlines()


