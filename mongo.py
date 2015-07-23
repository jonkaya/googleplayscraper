__author__ = 'akaya'

from settings import settings
import pymongo

def get_connection():
    if settings.MONGO_USER and settings.MONGO_PASSWD:
        return pymongo.MongoClient('mongodb://%s:%s@%s' % (settings.MONGO_USER, settings.MONGO_PASSWD, settings.MONGO_HOST), maxPoolSize=settings.MONGO_POOL_SIZE).googleplayscraper
    else:
        return pymongo.MongoClient('mongodb://%s' % (settings.MONGO_HOST), maxPoolSize=settings.MONGO_POOL_SIZE).googleplayscraper
