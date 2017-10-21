import requests
import json
from bs4 import BeautifulSoup


def get_request(url):
    
    page = requests.get(url);
    
    if (page.status_code == 200):
        return BeautifulSoup(page.content,'html.parser')
    else:
        return None


def get_rows(url, nb):
    
    soup = get_request(url)
    
    rows = soup.select("tbody tr")[0:nb] 
    order = [row.find("th").get_text() for row in rows]
    users = [row.find("a").get_text() for row in rows]
    
    #print(order + users)
    return rows, order, users


def get_api(user):
    url = "https://api.github.com/users/"+user+"/repos"
    header = {"Authorization" : "Basic mdp" }
    url = requests.get(url,headers = header)
    
    json_file = json.loads(url.content)
    favorites = [repos['stargazers_count'] for repos in json_file]
    print(favorites)        
    return 0
    
def main():
    
    url = "https://gist.github.com/paulmillr/2657075"
    contrib = 256
    get_request(url)
    users = get_rows(url, contrib)
    
    favorites = [get_api(user) for user in users]
    print(favorites)
if __name__ == "__main__": main()
