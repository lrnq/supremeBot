import requests
import bs4 as bs
from splinter import *


class supremeBot(object):
    def __init__(self, **info):
        self.base_url = 'http://www.supremenewyork.com/'
        self.shop = 'shop/all/'
        self.checkout = 'checkout/'
        self.info = info

    def initializeBrowser(self):
        self.path = {'executable_path': './chromedriver'}
        self.b = Browser('chrome', **path)

    def findProduct(self):
        r = requests.get(
            "{}{}{}".format(
                self.base_url,
                self.shop,
                self.info['category'])).text

        temp_tuple = []
        temp_link = []

        for link in soup.find_all('a', href=True):
            temp_tuple.append((link['href'], link.text))

        for i in temp_tuple:
            if i[1] == product or i[1] == color:
                temp_link.append(i[0])

        self.final_link = list(
            set([x for x in temp_link if temp_link.count(x) == 2]))[0]

    def visitSite(self):
        b.visit(
            "{}{}{}".format(
                self.base_url, self.shop, str(
                    self.final_link)))
        browser.find_option_by_text(size).click()
        browser.find_by_value('add to basket').click()

        time.sleep(0.5)
        browser.visit("{}{}".format(self.base_url, self.checkout))

        browser.fill("order[billing_name]", self.info['namefield'])
        browser.fill("order[email]", self.info['emailfield'])
        browser.fill("order[tel]", self.info['phonefield'])

        browser.fill("order[billing_address]", self.info['addressfield'])
        browser.fill("order[billing_city]", self.info['city'])
        browser.fill("order[billing_zip]", self.info['zipfield'])
        browser.select("order[billing_country]", self.info['country'])

        browser.select("credit_card[type]", self.info['card'])
        browser.fill("credit_card[cnb]", self.info['number'])
        browser.select("credit_card[month]", self.info['month'])
        browser.select("credit_card[year]", self.info['year'])
        browser.fill("credit_card[vval]", self.info['ccv'])
        browser.find_by_css('.terms').click()
        browser.find_by_value("process payment").click()

    def run(self):
        self.initializeBrowser()
        self.findProduct()
        self.visitSite()


if __init__ == "__main__":
    info = {
        "product" : "example",
        "color" : "example",
        "size" : "example",
        "category" : "example",
        "namefield" : "example",
        "emailfield" : "example@example.com",
        "phonefield" : "12345678910",
        "addressfield" : "example road",
        "city" : "example",
        "zip" : "example",
        "country" : "XX",
        "card" : "XXXX",
        "month" : "XX",
        "year" : "XXXX",
        "ccv" : "XXX"
    }
    bot = supremeBot(**info)
    bot.main()
