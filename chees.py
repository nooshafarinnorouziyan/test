import math
def chees(m,n):
    for i in range (m):
     for j in range (n):
        if(i+j)%2==0:
           print("*")
        else :
           print("#")
           print()