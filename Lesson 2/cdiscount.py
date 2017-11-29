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




url1 = getsearch('acer')
url2 = getsearch('dell')

r = requests.get(url1)
soup = BeautifulSoup(r.text, 'html.parser')
machine = soup.tbody.find_all(class_= 'price')
machine_raw = [m.text.split(' ', 1)[0] for m in machine]
print(machine_raw)

r = requests.get(url1)
soup = BeautifulSoup(r.text, 'html.parser')
machine = soup.tbody.find_all(class_= 'prdtPrSt')
machine_raw = [m.text.split(' ', 1)[0] for m in machine]
print(machine_raw)

r = requests.get(url2)
soup = BeautifulSoup(r.text, 'html.parser')
machine = soup.tbody.find_all(class_= 'price')
machine_raw = [m.text.split(' ', 1)[0] for m in machine]
print(machine_raw)

r = requests.get(url2)
soup = BeautifulSoup(r.text, 'html.parser')
machine = soup.tbody.find_all(class_= 'prdtPrSt')
machine_raw = [m.text.split(' ', 1)[0] for m in machine]
print(machine_raw)

print("Marque = ")
print("Prix = ")
print("Solde = ")