import requests
from bs4 import BeautifulSoup

def GetRequest():
    page = requests.get("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2010")
    page1 = requests.get("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2011")
    page2 = requests.get("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2012")
    page3 = requests.get("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2013")
        
    listeGetQuery= []
    listeGetQuery.append(page)
    listeGetQuery.append(page1)
    listeGetQuery.append(page2)
    listeGetQuery.append(page3)
              
    return listeGetQuery

def GetData(page):
    number_class = "montantpetit G"
    
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.find_all(class_= number_class)
    
    price_text = soup.find_all(class_= number_class)
    data = price_text[1]
    data1 = price_text[4]
    data2 = price_text[10]
    data3 = price_text[13]
    #print(data.prettify())
    listeNumber = []
    listeNumber.append(data.text.strip())
    listeNumber.append(data1.text.strip())
    listeNumber.append(data2.text.strip())
    listeNumber.append(data3.text.strip())
    print('Euros par habitants : ')
    print(listeNumber)
    
    strate_class = "montantpetit G"
    
    soup.find_all(class_= number_class)
    
    price_text = soup.find_all(class_= strate_class)
    data = price_text[2]
    data1 = price_text[5]
    data2 = price_text[11]
    data3 = price_text[14]
    #print(data.prettify())
    listeStrate = []
    listeStrate.append(data.text.strip())
    listeStrate.append(data1.text.strip())
    listeStrate.append(data2.text.strip())
    listeStrate.append(data3.text.strip())
    print('Moyenne par strate : ')
    print(listeStrate)
    print(+ "\n")

    return

def main():

    GetRequest()  
    
    listeUrl = []
    listeUrl.append("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2010")
    listeUrl.append("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2011")
    listeUrl.append("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2012")
    listeUrl.append("http://alize2.finances.gouv.fr/communes/eneuro/detail.php?icom=056&dep=075&type=BPS&param=5&exercice=2013")
    
    print("Voici les données de l'an 2010 :" + "\n")
    GetData(page)
    print("Voici les données de l'an 2011 :" + "\n")
    GetData(page1)
    print("Voici les données de l'an 2012 :" + "\n")
    GetData(page2)
    print("Voici les données de l'an 2013 :" + "\n")
    GetData(page3)

if __name__ == "__main__": main()

