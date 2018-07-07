import requests
import bs4 as bs
from splinter import Browser


path = {'executable_path':'./chromedriver'}
b = Browser('chrome', **path)

b.visit('http://endclothing.com/dk/footwear')
print(b.html)
