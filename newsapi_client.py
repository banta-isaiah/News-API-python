import os
import requests

NEWS_API_KEY = os.environ.get('NEWS_API_KEY', None)

class NewsAPI:

    base_url = 'https://newsapi.org/v2/' 

    def get_top_headlines(self):
        pass


    def get_everything(self):
        pass

    
    def get_sources(self):
        pass



        

    





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


