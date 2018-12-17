'''->Sometimes we can declare a function without any name,such type of nameless functions
are called anonymous functions or lambda functions.
The main purpose of anonymous function is just for instant use(i.e for one time usage)'''
#normally we can use 'def' keyword
def square(a):
    print(a*a)
square(10)

#now using lambda-keyword
#ex:- square
a=lambda n:n*n
print(a(2))

#ex:- addition
a=lambda x,y:x+y
print(a(10,20))

#ex:- greatest number
a=lambda x,y:x if x>y else y
print(a(10,20))

#ex:- even or odd using 'filter'
a=[1,2,3,4,5,6,7,8,9,10,11]
b=list(filter(lambda a:a%2==0,a))
print(b)
c=list(filter(lambda a:a%2!=0,a))
print(c)
