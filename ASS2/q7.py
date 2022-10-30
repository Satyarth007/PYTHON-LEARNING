import math

def areaTriangle(a,b,c):
    s= (a+b+c)/2
    a = math.sqrt(s* (s-a)*(s-b)*(s-c)) #Heron's formula
    return a

def main():
    a = float(input("ENTER A :- "))
    b = float(input("ENTER B :- "))
    c = float(input("ENTER C :- "))

    assert (a+b > c) and (a+c >b) and (b+c >a)

    print("AREA OF TRIANGLE IS :- ",areaTriangle(a,b,c))

main()
