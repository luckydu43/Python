
import asyncio


async def add(a,b):
    await asyncio.sleep(0.5)
    return a+b

def toto():
    pass

async def Etape15():
    print(50*'-')
    print ("Co-routines")
    print(50*'-')

    print ("Hello...")
    await asyncio.sleep(1)
    print ("... World!")

    r = await add(1,2)
    print(r)

    all_r = [add(1,2), add(18,25), add(18, 42), add(1, 28)]
    r = await asyncio.gather(*all_r)
    print(r)
    
if __name__ == "__main__":
    asyncio.run(Etape15())