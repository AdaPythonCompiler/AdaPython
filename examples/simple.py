import sys
def procedureGreet():
    A : int = 0
    B: list = [x for x in range(0, 12)]
    if A==0:
        print("A is zero")
    elif A>0:
        print("A is positive")
    elif A==1:
        print("A is positive")
    else:
        print("A is not zero")
    print("Hello, world!")
def procedureMain():
    I : int = 1
    while I<=10:
        print("Hello, world!")
        I = I+1
    print("Hello, world!")
def procedureMainFor():
    for I in range(1, 11):
        print("Hello, world!")
    print("Hello, world!")
def procedureMainCase():
    I : int = 1
    if I == 1:
        print("I is 1")
    elif I == 2:
        print("I is 2")
    elif I == 3:
        print("I is 3")
    else:
        print("I is others")
if __name__ == '__main__':
    procedureGreet()
    procedureMain()
    procedureMainFor()
    procedureMainCase()