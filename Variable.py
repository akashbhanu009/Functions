'''There was two type of variable available in PYTHON
First=> GLOBAL Variable; Second=> LOCAL Variable
The variables which are declared outside of function are called global variables.
These variables can be accessed in all functions of that module.
'''
'''a=10 #global-variable
def f1():
    print(a)
def f2():
    print(a)
f1()
f2()'''

'''The variables which are declared inside a function are called local variables.
->Local variables are available only for the function in which we declared it.i.e from outside of function we cannot access.
'''
'''def f1():
    a=20
    print(a) #Valid
def f2():
    print(a) #Invalid, give an error 'a' is not defined
f1()
f2()'''

#Using 'global' keyword
'''a=10 #global variable
def f1():
    global a
    a=777
    print(a) #777
def f2():
    print(a) #access function global-variable; output-> 777
f1()
f2()'''

'''Note: If global variable and local variable having the same name 
then we can access global variable inside a function as follows.'''
'''ex:-
a=10 #global-variable
def f1():
    a=777
    print(a) #output-> 777
    print(globals()['a']) #output-> 10
f1()'''

'''ex:-
a=10 #global variable
b=20 #global variable
def f1():
    # global a
    a=777 #local variable
    print(a)
    print(globals()['a'])
    print(globals()['b']
def f2():
    print(a)
    print(globals()['a'])
f1()
f2()'''
a=1
def f1():
    a=2
    print("Global-Variable=> ",globals()['a'])
    print("Local-Variable=> ",locals()['a'])
f1()