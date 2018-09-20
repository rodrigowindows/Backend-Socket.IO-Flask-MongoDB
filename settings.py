import os

class Config(object):
    """Base configuration."""
    DEBUG = True
    MONGO_URI = "mongodb://localhost:27017/myDatabase" #app.config.get('MONGO_URI')



