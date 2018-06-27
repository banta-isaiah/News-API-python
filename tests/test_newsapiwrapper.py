from Client import NewsAPI

def test_get_everything():
    """Tests an API call to get all news articles associated with a keyword or other value"""

    news_api_instance = NewsAPI()
    json_object = news_api_instance.get_everything(q = 'bitcoin')
    
    assert isinstance(response, dict)

