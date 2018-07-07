import requests
import bs4 as bs
from splinter import *

parser = argparse.ArgumentParser()
parser.add_argument(
    "-p",
    "--product",
    required=True,
    help="Name of product")
parser.add_argument(
    "-s",
    "--size",
    required=True,
    help="Size of product")
parser.add_argument(
    "-c",
    "--color",
    required=True,
    help="Year of copyright for LICENSE")
parser.add_argument("-cat", "--category", required=True,
                    help="Author of library for LICENSE")
parser.add_argument(
    "-n",
    "--namefield",
    required=True,
    help="Name of product")
parser.add_argument(
    "-e",
    "--emailfield",
    required=True,
    help="Size of product")
parser.add_argument(
    "-p",
    "--phonefield",
    required=True,
    help="Year of copyright for LICENSE")
parser.add_argument("-a", "--addressfield", required=True,
                    help="Author of library for LICENSE")

parser.add_argument(
    "-ci",
    "--city",
    required=True,
    help="Name of product")
parser.add_argument(
    "-cou",
    "--country",
    required=True,
    help="Size of product")
parser.add_argument(
    "-z",
    "--zip",
    required=True,
    help="Year of copyright for LICENSE")
parser.add_argument("-cat", "--category", required=True,
                    help="Author of library for LICENSE")
parser.add_argument(
    "-ca",
    "--card",
    required=True,
    help="Name of product")
parser.add_argument(
    "-cn",
    "--number",
    required=True,
    help="Size of product")
parser.add_argument(
    "-y",
    "--year",
    required=True,
    help="Year of copyright for LICENSE")
parser.add_argument(
    "-m",
    "--month",
    required=True,
    help="Author of library for LICENSE")
parser.add_argument(
    "-cc",
    "--ccv",
    required=True,
    help="Author of library for LICENSE")


class supremeBot(object):
    def __init__(self, flags):
        self.flags = flags
        self.base_url = 'http://www.supremenewyork.com/'
        self.shop = 'shop/all/'
        self.checkout = 'checkout/'

    def initializeBrowser(self):
        self.path = {'executable_path': './chromedriver'}
        self.b = Browser('chrome', **path)

    def findProduct(self):
        r = requests.get(self.flags.url).text

        temp_tuple = []
        temp_link = []

        for link in soup.find_all('a', href=True):
            temp_tuple.append((link['href'], link.text))

        for i in temp_tuple:
            if i[1] == self.flags.product or i[1] == self.flags.color:
                temp_link.append(i[0])

        self.final_link = list(
            set([x for x in temp_link if temp_link.count(x) == 2]))[0]

    def visitSite(self):
        b.visit(
            "{}{}{}".format(
                self.base_url, self.shop, str(
                    self.final_link)))
        browser.find_option_by_text(self.flags.size).click()
        browser.find_by_value('add to basket').click()

        time.sleep(0.5)
        browser.visit("{}{}".format(self.base_url, self.checkout))

        browser.fill("order[billing_name]", self.flags.namefield)
        browser.fill("order[email]", self.flags.emailfield)
        browser.fill("order[tel]", self.flags.phonefield)

        browser.fill("order[billing_address]", self.flags.addressfield)
        browser.fill("order[billing_city]", self.flags.city)
        browser.fill("order[billing_zip]", self.flags.zipfield)
        browser.select("order[billing_country]", self.flags.country)

        browser.select("credit_card[type]", self.flags.card)
        browser.fill("credit_card[cnb]", self.flags.number)
        browser.select("credit_card[month]", self.flags.month)
        browser.select("credit_card[year]", self.flags.year)
        browser.fill("credit_card[vval]", self.flags.ccv)
        browser.find_by_css('.terms').click()
        browser.find_by_value("process payment").click()

    def run(self):
        self.initializeBrowser()
        self.findProduct()
        self.visitSite()


def main(self):
    args = parser.parse_args()
    cmd = structureGenerator(args)
    cmd.run()


if __init__ == "__main__":
    main()
