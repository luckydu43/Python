
from Rectangle import Rectangle

def test():
    print("avant :", Rectangle.get_nombre_instances())
    Etape10()
    print("Apres :", Rectangle.get_nombre_instances())

def Etape10():
    r1 = Rectangle(1,2)
    r2 = Rectangle(2,3)
    print ("Pendant :", Rectangle.get_nombre_instances())

    rectangle2 = Rectangle.build_from_str("4,8")
    print(rectangle2)
if __name__ == "__main__":
    test()