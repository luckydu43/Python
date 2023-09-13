from collections.abc import Callable, Iterable, Mapping
from multiprocessing import Pool
import os
import threading
import time
from typing import Any

semaphore = threading.Lock()

# Methode threadée avec sémaphore
def traitement_long_1():
    with semaphore:
        for i in range(5):
            print(f"traitement_long_1 {i} - {threading.current_thread()}")

# Methode threadée avec sémaphore
def traitement_long_2():
    with semaphore:
        for i in range(5):
            print(f"traitement_long_2 {i} - {threading.current_thread()}")

# classe proposant une méthode threadée sans sémaphore
class TheThread(threading.Thread):
    def __init__(self) -> None:
        super().__init__(
        )

    def run(self) -> None:
        for i in range(5):
            print(f"run {i} - {self.name}")



def Etape14():
    print(50*'-')
    print ("Multiprocessing avec semaphores")
    print(50*'-')
    thread1 = threading.Thread(target=traitement_long_1)
    thread2 = threading.Thread(target=traitement_long_2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    TheThread1 = TheThread()
    TheThread2 = TheThread()
    TheThread1.start()
    TheThread2.start()
    TheThread1.join()
    TheThread2.join()
    # Mettre un join permet à la méthode Etape14 d'attendre la fin d'exécution de son thread
    print("Fin des threads")

if __name__ == "__main__":
    start = time.perf_counter()
    Etape14()
    print(time.perf_counter() - start)