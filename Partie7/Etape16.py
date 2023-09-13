import time
from bs4 import BeautifulSoup
import asyncio
import httpx



async def save(save_queue):
    while True:
        data = await save_queue.get()

async def download_Url(url, semaphore):
    async with semaphore:
        async with httpx.AsyncClient() as asyncClient:
            response = await asyncClient.get(url)
            with open (url.split('/')[-1], 'w') as f:
                f.write(response.text)

async def Etape12():
    print(50*'-')
    print ("Scrapper une page HTML avec des co-routines")
    print(50*'-')
    
    start= time.perf_counter()
    url="http://logs.eolem.com/"
    semaphore = asyncio.Semaphore(5)
    response = httpx.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    all_a = [url+link.get('href') for link in soup.find_all('a') if ".log" in link.get('href')]
    print(all_a)
    
    all_download = [download_Url(url,semaphore) for url in all_a]
    await asyncio.gather(*all_download)

 
    print("Temps passé :", float(time.perf_counter()-start).__round__(2), 'secondes')
if __name__ == "__main__":
    asyncio.run(Etape12())