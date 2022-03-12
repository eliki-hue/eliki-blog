from distutils.command.config import config


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/v2/top-headlines/{}?apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options ={
    'development':DevConfig,
    'production':ProdConfig
}

    # https://newsapi.org/v2/top-headlines/sources=bbc?apiKey=bb5dc174241747118fdf8b391701fbe9
    #GET https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=bb5dc174241747118fdf8b391701fbe9