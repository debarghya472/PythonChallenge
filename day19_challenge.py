import math

def perfectSquares(a,b):
    while a<=b:
        i=math.sqrt(a)
        if (i - math.floor(i)) == 0 :
            print(a)
        a+=1

u= int(input ("enter upper range : "))
l=int(input("Enter lower range : "))

perfectSquares(l,u)