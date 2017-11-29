import requests
from bs4 import BeautifulSoup


def getsearch(search):
    url = 'https://www.cdiscount.com/search/10/' + search + '.html#_his_'
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup
    else:
        return None


def getInfoFromOneProductSoup():

    price
PrintInfoForWholeSearchPage('acer')
print('\n' + '=' * 50)
PrintInfoForWholeSearchPage('dell')
