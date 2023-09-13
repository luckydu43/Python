from multiprocessing import Pool
import os
import time


def f(x) :
    t = 1
    start = time.time()
    while time.time() - start < t:
        pass
    return x*x


def Etape13():
    print(50*'-')
    print ("Multiprocessing")
    print(50*'-')
    print(os.cpu_count())
    with Pool(61) as p:
        print(p.map(f, [1,10]))

	
if __name__ == "__main__":
    start = time.perf_counter()
    Etape13()
    print(time.perf_counter() - start)