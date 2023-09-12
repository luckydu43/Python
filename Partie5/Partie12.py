import time
from bs4 import BeautifulSoup
import requests

def download_Url(url):
    response = requests.get(url)
    with open (url.split('/')[-1], 'w') as f:
        f.write(response.text)

def Etape12():
    start= time.perf_counter()
    print(50*'-')
    print ("Scrapper une page HTML")
    print(50*'-')
    url="http://logs.eolem.com/"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    #Facon liste par intention
    #all_a = [f"{url}{link.get('href')}" for link in soup.find_all('a') if ".log" in link.get('href')]

    #Facon lisible
    all_a = [url+link.get('href') for link in soup.find_all('a') if ".log" in link.get('href')]
    print(all_a)
    ## Facon simple
    #for link in soup.find_all('a'):
    #    if not str(link.get('href')).startswith('?'):
    #        print(link.get('href'))

    for url_log in all_a:
        download_Url(url_log)
    print("Temps passé :", float(time.perf_counter()-start).__round__(2), 'secondes')
if __name__ == "__main__":
    Etape12()