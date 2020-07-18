import math


def isperfectsq(n):
    sr=math.sqrt(n)
    
    return((sr-math.floor(sr))==0)

x=int(input())
if(isperfectsq(x)):
    print("Yes")
else:
    print("No")
