import time
from bs4 import BeautifulSoup
import asyncio
import httpx


async def download_Url_queues(download_queue:asyncio.Queue, save_queue:asyncio.Queue):
    while True:
        data = await download_queue.get()
        async with httpx.AsyncClient() as asyncClient:
            response = await asyncClient.get(data)
            to_save = {
                "text":response.text,
                "file_log":data.split('/')[-1]
            }
            save_queue.put_nowait(to_save)

        download_queue.task_done()


async def save(save_queue):
    while True:
        data = await save_queue.get()
        with open (data['file_log'], 'w') as f:
            f.write(data['text'])
        save_queue.task_done()

async def Etape17():
    print(50*'-')
    print ("Scrapper une page HTML avec des queues asynchrones")
    print(50*'-')
    
    start= time.perf_counter()

    url="http://logs.eolem.com/"
    response = httpx.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    all_a = [url+link.get('href') for link in soup.find_all('a') if ".log" in link.get('href')]
    print(all_a)

    download_queue = asyncio.Queue()
    save_queue = asyncio.Queue()
    
    nb_download_workers = 5
    download_tasks = []
    for i in range(nb_download_workers):
        task = asyncio.create_task(download_Url_queues(download_queue, save_queue))
        download_tasks.append(task)

    nb_save_workers = 3
    save_tasks = []
    for i in range(nb_save_workers):
        task = asyncio.create_task(save(save_queue))
        save_tasks.append(task)
    
    for url in all_a:
        download_queue.put_nowait(url)
    
    await download_queue.join()
    await save_queue.join()

    [task.cancel() for task in download_tasks]
    [task.cancel() for task in save_tasks]
    
    print("Temps passé :", float(time.perf_counter()-start).__round__(2), 'secondes')
if __name__ == "__main__":
    asyncio.run(Etape17())