#There was four type's of ARGUMENTS, maintain there orders compulsory....
# 1. Positional Arguments 2. Keyword Arguments 3.Default Arguments 4.Variable-Length Arguments
#POSITIONAL ARGUMENTS===>
def sub(a,b):
    print(a-b)
sub(100,200)
sub(200,100)

#Keyword Arguments
def wish(name,msg):
    print("hello\t",name,"\t",msg)
wish("sweety","how are you doing") #POSITIONAL ARGUMENT
wish(name="rakesh",msg="what are you doing")#KEYWORD ARGUMENT
wish("bhanu",msg="where are you")#using in-order (1).Positional Argument then (2).Keyword Argument
# wish(msg="are you searching for a job","akash")#raise an error positional arguments come after the keyword arguments

#Default Arguments
def wish(name="Guest"):
    print("Hello",name,"Good Morning")
wish("AKASH")#here give the value then it response as the given value
wish()#not give any value, so it take's the default value as 'Guest' which was already given at the time of function define

#Variable-Length Arguments
def varlen(*n):
    total=0
    for i in n:
        total=total+i
        print(total)
varlen()
varlen(10)
varlen(10,20)
varlen(10,20,30)
varlen(0,10,20,30,40)

#NOTE: in arguments always use serial order i.e Positional; Keyword; Default; Varable-Length. Otherwise you will get an error
