'''def wish(name):
    print("Hello,", name,"How are you doing")

wish("akash")
wish("Bhanu")
wish("Tiwari")
'''

'''def number(n):
    print("The square of\t",n,"=>\t",n*n)

number(10)
number(11)
'''

def number():
    n=int(input("Enter a number=>\t"))
    if n%2==1:
        print(n,"is prime number")
    elif n%2==0:
        print(n,"is EVEN number")
    else:
        print(n,"is  ODD number")
number()
