# math = int(input())
# phy = int(input())
# chem = int(input())

# avg = (math + phy + chem)/3

# if avg >= 90:
#     print('Excellent')
# elif avg < 90  and avg >= 80:
#     print('Very good')
# elif avg < 80 and avg >= 70:
#     print('good')
# else:
#     print('Need Pratice')

# a, b, c = int(input("Enter A:")), int(input("Enter B:")), int(input("Enter C:"))

# if a > b and a > c:
#     print(a,"is greater")

# elif b > a and b > c:
#     print(b,"is greater")

# else:
#     print(c,"is greater")

# bp = int(input("Enter Your basic pay:"))

# hra = (bp*15)/100
# print("hra:",hra)

# da, it = 0,0

# if bp > 50000:
#     da=(bp*10)/100
# elif bp > 30000 and bp <= 50000:
#     da=(bp*15)/100
# else:
#     da=(bp*20)/100

# print("da:",da)

# gross_sal = bp+da+hra
# print("gross_sal:",gross_sal)

# if gross_sal>100000:
#     it = (gross_sal*30)/100
# elif gross_sal >= 50000 and gross_sal<100000:
#     it = (gross_sal*10)/100
# elif gross_sal<50000:
#     it=0

# print('it:',it)

# net_sal = gross_sal - it

# print(net_sal)

# 1)Prime no between two numbers
# a, b = int(input("Enter A:")), int(input("Enter B:"))

# for i in range(a,b+1):
#     t=True
#     for j in range(2, i//2+1):
#         if i%j==0:
#             t=False
#             break

#     if t==True:
#         print(i,end=" ")

# 2)
# a=int(input())
# i,c=2,1

# while(c<=a):
#     t=True
#     for j in range(2, i//2+1):
#         if i%j==0:
#             t=False
#             break
    
#     if t==True: 
#         print(i,end=' ')
#         c+=1
#     i+=1

# print all factorial in the given range(2-10)
# reverse the string or reverse the no
# print the armstrong no in given range
'''
string='python programming'
#slicing
print(string[0:5:2])
print(string[:5])
print(string[::2])
print(string[::-1])
print(dir(string))
print(string.upper())
print(string.lower())
print(string.strip())

string='pythonprogramming'
print(string.capitalize())
print(string.title())
print(string.isalpha())
print(string.isdigit())
print(string.startswith('p'))
print(string.endswith('p'))
print(string.replace('p','P'))
print(string.find('z'))
print(max(string))
print(min(string))

string='python programming concepts'
l=string.split()
print(l)
#l=['D','e','l','h','i']
print(' '.join(l))

string='python programming concepts'
print(''.join(sorted(string)))
print(string[::-1])

#function

#1. builtin function(print(),input(),type(),id(),len(),max(),min())
#2. user-defined function:defined by the programmer


def isPrime():
    n=int(input('Enter any no: '))
    f=True
    for i in range(2,n//2+1):
        if n%i==0:
            f=False
            break

    if f==True:
        print('No is prime')
    else:
        print('No is not prime')

isPrime()

def sum():
    a=10
    b=20
    print(a+b)
sum()



1. default
2. parametrised
   a. positional arguments
   b. default arguments
   c. keyword arguments
   d. variable length positional arguments
   e. varaible length keyword arguments



def sum():
    a=10
    b=20
    print(a+b)
'
#parametrised
def sum(a,b):
   print(a+b)

sum(100,200)

2. parametrised
   a. positional arguments
   b. default arguments
   c. keyword arguments
   d. variable length positional arguments
   e. varaible length keyword arguments


#a. positional arguments
def sum(a,b):
   print(a+b)

sum(100,200)

#b. default arguments

def sum(a=10,b=20):
   print(a+b)

sum()

# c. keyword arguments
def fun(b,a):
    print(a,b)

fun(a=10,b=20)

d. variable length positional arguments
def sum(*args):
    for i in args:
        print(i)

sum(10,20,30,40,50,60)

#e.varaible length keyword arguments
def sum(**args):
    for k,v in args.items():
        print(k,v)

sum(amit=101,sumit=102)


def sum(a,b):
    return a+b

sum=sum(100,200)
print(sum)

def sum(a,b):
    return a+b,a-b

sum,sub=sum(100,200)
print(sum,sub)

# with argument with return
# with argument without return
# no argument no return
# no argument with return

uname='xyz@abc'
passd='123456'

def userValidation(un,pa):

    if un==uname and pa==passd:
        print('Login Successful:')
    else:
        print('Try Again:')


un=input('Uname:')
pas=input('Pass:')
userValidation(un,pas)


from mycalculator import add,mul
print(add(1000,2000))
print(mul(1000,2000))

from mycalculator import *
print(add(1000,2000))
print(mul(1000,2000))
from mycalculator import add,mul
print(sub(1000,2000))
print(div(1000,2000))
print(myvar)



import mycalculator
print(mycalculator.add(10,20))


# string,slicing,function,types of function,arguments type,module,inbuilt module

#class and object


# object oriented programming(OOP)

# class,object,encapsulation,inheritance,polymorphism,abstraction

#c++=>oops
#java=>oops
#python=>oops
'''
#car
#person
#mobile

#static function,static var,abstract class,type of variable in the class,inheritance,
# a,b=int(input("A:")),int(input("B:")),

# def sum(a,b):
#     return a+b

# def diff(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     return a//b

# def mod(a,b):
#     return a%b

# print("The sum:",sum(a,b))
# print("The diff:",diff(a,b))
# print("The mul:",mul(a,b))
# print("The div:",div(a,b))
# print("The mod:",mod(a,b))

# def check(uname,password):
#     if uname == 'xyz@abc' and password == '123456':
#         return True
#     else: return False

# uname, password = input('Enter Username: '), input('Enter Password: ')

# if check(uname,password):
#     print("Login success")

# else: print("Wrong Crenditials")


# import math
# print(math.pi)
# print(math.floor(10.5))
# print(math.ceil(10.5))
# print(math.sqrt(10))
# print(math.pow(10,2))
# print(math.exp(2))#e=2.71
# print(math.factorial(10))


# class Student:
#     def _init_(self):#default constructor
#         self.roll=''
#         self.name=''
#         self.mail=''
#         print('Hi welcome to my class:')

#     def getData(self):
#         self.roll=input('Roll No: ')
#         self.name=input('Name : ')
#         self.mail=input('Email Id: ')
#     def putData(self):
#         print(f'Roll No: {self.roll}')
#         print(f'Name : {self.name}')
#         print(f'Email Id: {self.mail}')

# obj1=Student()
# obj1.putData()
# obj1.getData()
# obj1.putData()

# class employee:
#     def __init__(self):
#         self.name=''
#         self.age=''
#         self.salary=''
#         self.dept=''
#         self.city=''

#     def inputFun(self):
#         self.name=input('Enter Name: ')
#         self.age=int(input('Enter age: '))
#         self.salary=int(input('Enter salary: '))
#         self.dept=input('Enter dept: ')
#         self.city=input('Enter city: ')
    
#     def showFun(self):
#         print('Name: ',self.name)
#         print('Age: ',self.age)
#         print('Salary: ',self.salary)
#         print('Dept: ',self.dept)
#         print('City: ',self.city)

# s=employee()
# s.inputFun()
# s.showFun()
