#!/usr/bin/env python3
import requests
import bs4 as bs
from splinter import Browser
import helpers


class supremeBot(object):
    def __init__(self, **info):
        self.base_url = 'http://www.supremenewyork.com/'
        self.shop = 'shop/all/'
        self.checkout = 'checkout/'
        self.info = info

    def initializeBrowser(self):
        driver = self.info["driver"]
        path = helpers.get_driver_path(driver)
        if driver == "geckodriver":
            self.b = Browser()
        elif driver == "chromedriver":
            executable_path = {"executable_path": path}
            self.b = Browser('chrome', **executable_path)


    def findProduct(self):
        r = requests.get(
            "{}{}{}".format(
                self.base_url,
                self.shop,
                self.info['category'])).text
        soup = bs.BeautifulSoup(r, 'lxml')

        temp_tuple = []
        temp_link = []

        for link in soup.find_all('a', href=True):
            temp_tuple.append((link['href'], link.text))
        for i in temp_tuple:
            if i[1] == self.info['product'] or i[1] == self.info['color']:
                temp_link.append(i[0])

        self.final_link = list(
            set([x for x in temp_link if temp_link.count(x) == 2]))[0]

    def visitSite(self):
        self.b.visit(
            "{}{}".format(
                self.base_url, str(
                    self.final_link)))
        self.b.find_option_by_text(self.info['size']).click()
        self.b.find_by_value('add to basket').click()

    def checkoutFunc(self):

        self.b.visit("{}{}".format(self.base_url, self.checkout))

        self.b.fill("order[billing_name]", self.info['namefield'])
        self.b.fill("order[email]", self.info['emailfield'])
        self.b.fill("order[tel]", self.info['phonefield'])

        self.b.fill("order[billing_address]", self.info['addressfield'])
        self.b.fill("order[billing_city]", self.info['city'])
        self.b.fill("order[billing_zip]", self.info['zip'])
        self.b.select("order[billing_country]", self.info['country'])

        self.b.select("credit_card[type]", self.info['card'])
        self.b.fill("credit_card[cnb]", self.info['number'])
        self.b.select("credit_card[month]", self.info['month'])
        self.b.select("credit_card[year]", self.info['year'])
        self.b.fill("credit_card[vval]", self.info['ccv'])
        self.b.find_by_css('.terms').click()
        #self.b.find_by_value("process payment").click()

    def main(self):
        self.initializeBrowser()
        self.findProduct()
        self.visitSite()
        self.checkoutFunc()


if __name__ == "__main__":
    INFO = {
        "driver": "geckodriver",
        "product": "S/S Pocket Tee",
        "color": "Black",
        "size": "Medium",
        "category": "tops_sweaters",
        "namefield": "example",
        "emailfield": "example@example.com",
        "phonefield": "XXXXXXXXXX",
        "addressfield": "example road",
        "city": "example",
        "zip": "72046",
        "country": "GB",
        "card": "visa",
        "number": "1234123412341234",
        "month": "09",
        "year": "2020",
        "ccv": "123"
    }
    BOT = supremeBot(**INFO)
    BOT.main()
