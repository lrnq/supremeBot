import requests
import bs4 as bs
from splinter import *


class sneakerBot(object):
    def __init__(self, flags):
        self.flags = flags

    def initializeBrowser(self):
        self.path = {'executable_path' : './chromedriver'}
        self.b = Browser('chrome', **path)

    def findSneaker(self):
        r = requests.get(self.flags.url).text


