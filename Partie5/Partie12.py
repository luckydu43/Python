from multiprocessing.pool import ThreadPool
import threading
import time
from bs4 import BeautifulSoup
import requests

def download_Url(url):
    response = requests.get(url)
    with open (url.split('/')[-1], 'w') as f:
        f.write(response.text)

def Etape12():
    print(50*'-')
    print ("Scrapper une page HTML avec un pool de threads")
    print(50*'-')
    
    start= time.perf_counter()
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

    with ThreadPool(61) as threadpool:
        threadpool.map(download_Url, all_a)
        
    """
    threads = []

    for url_log in all_a:
        
        # Avec Thread
        thread = threading.Thread(target=download_Url,args=[url_log])
        thread.start()
        threads.append(thread)

        # Sans Thread
        # download_Url(url_log)
    for thread in threads:
        thread.join()
    """
    print("Temps passé :", float(time.perf_counter()-start).__round__(2), 'secondes')
if __name__ == "__main__":
    Etape12()