from math import *
n=int(input("Enter the number to find FACTORIAL=>\t"))
a=n*factorial(n-1)
print(a)

#One-Method to find FACTORIAL
'''def fact(n):
    result=1
    while n>=1:
        result=result*n
        n=n-1
        if (n==0):
            return result
for i in range(1,5):
    print(i,fact(i))
'''



