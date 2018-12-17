'''a=10
b=20#global variable
def f1():
    # global a
    a=777 #local variable
    print(a)
    print(globals()['a'])
    print(globals()['b'])
def f2():
    print(a)
    print(globals()['a'])
f1()
f2()'''

'''a=input("Enter a word to chech whether it's PALINDROME or not=>\t")
if a==a[::-1]:
    print('yes')
else:
    print("no")'''
def outer():
    print("outer function started")
    def inner():
        print("Inner function executed")
        print("outer function calling inner function")
    return inner()
fi=outer
fi()
