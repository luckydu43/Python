import unmodule

def test():
    valeur = 10
    print(valeur)
    print('nom test : ' + __name__)
    unmodule.hello()
    a=1
    print('a = ' + str(a) + ', id = ' + str(hex(id(a))))
    a=23304689730942085
    print('a = ' + str(a) + ', id = ' + str(hex(id(a))))
    b=23304689730942085
    print('b = ' + str(b) + ', id = ' + str(hex(id(b))))
    c=23304689730942085
    print('c = ' + str(c) + ', id = ' + str(hex(id(c))))
if __name__ == "__main__":
    test()