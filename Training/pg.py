'''
#variable in the class:instance variable,class,private and protected
class X:
    c=0

    def _init_(self):
        self.a=0
        self.b=0
        self.__pri=100
        self._pro=200
    def show(self):
        print(X.c)
        print(self.a)
        print(self.b)
        #print(self.__pri)
        #print(self._pro)
obj=X()
#obj.show()
print(X.c)
print(obj.a)
print(obj.b)
#print(obj.__pri)
#print(obj._pro)


#function or method of the class:instance,class,static,setter,getter
class fun_class:
    def fun_ins(self):
        self.a=0
        print('Hi you are in fun(instance function')
    @classmethod
    def fun_class(cls):
        print('Hi you are in fun(class function')
    @staticmethod
    def fun_static():
        print('Hi you are in fun(static function')
    def setData(self,val):
        self.a=val
    def getData(self):
        return self.a


obj=fun_class()
obj.fun_ins()
fun_class.fun_class()
fun_class.fun_static()
obj.setData(100)
print(obj.getData())



class count:
    counter=0
    def _init_(self):
        print('Hi')
        self.c=0
        self.c =self.c+1
        count.counter+=1
obj1=count()
obj2=count()
obj3=count()
print(count.counter)
print(obj1.c)
print(obj2.c)
print(obj3.c)


# Inheritance:

class X:
    def _init_(self):
        self.a=100
    def fun(self):
        print(self.a)
class Y(X):
    def _init_(self):
        super()._init_()
        self.b=200

    def foo(self):
        print(f'b= {self.b}, a= {self.a}')
obj=Y()
obj.foo()
#obj.fun()


class x:
    def _init_(self):
        print('welcome to x class')
    def x_fun(self):
        print('welcome x function')
class y():
    def  _init_(self):
        super()._init_()
        print('welcome to y class')
    def y_fun(self):
        print('welcome y function')
class z(x,y):
    def  _init_(self):
        super()._init_()
        super(x,self)._init_()
        print('welcome to z class')
    def z_fun(self):
        print('welcome z function')

obj=z()
obj.z_fun()
obj.y_fun()
obj.x_fun()

Types: single,multiple,multilevel,heirarchical


class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass

class X:
    pass
class Y(X):
    pass
class Z(X):
    pass


# data overriding
class X:
    def _init_(self):
        self.a=100

class Y(X):
    def _init_(self):
        self.a=200
    def show(self):
        print(self.a)#derived class variable
        print(X().a)#base class variable
obj=Y()
obj.show()


class X:
    def _init_(self):
        self.a=100
    def show(self):
        print('X show')
class Y(X):
    def _init_(self):
        super()._init_()
        self.a=200
    def show(self):
        X.show(self)
        print(X().a)
        print(self.a)
obj=Y()
obj.show()



from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def _init_(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*(self.radius**2)

class Rectangle(Shape):
    def _init_(self,l,w):
        self.len=l
        self.wid=w
    def area(self):
        return self.len*self.wid

#o=Shape()#create the object Abstract class
o1=Circle(10)
print(o1.area())
o2=Rectangle(5,10)
print(o2.area())



from  myclassfile import *

class Z(x,y):
    def _init_(self):
        self.a=100
        super()._init_();
        super(x,self)._init_()
    def z_fun(self):
        print(self.a)
obj=Z()
obj.z_fun()
obj.x_fun()
obj.y_fun()


from  myclassfile import x
obj=x()
obj.x_fun()



l=[1,2,3,4]
a=2
z=100
d={1:'A',2:'B'}
try:
    x=10/a
    print(l[1])
    print(z)
    print('a'+'10')
    print(d[1])
    print('..............')
    print('Done..')
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
except TypeError as e:
    print(e)
except KeyError as e:
    print(e,'Error')
else:
    print('Hey every thing is fine go ahead...')
finally:
    print('Hey bye bye..')


#exception:safe the program from unsual logic
a=100
b=2
l=[1,2,3,4,5]
d={1:'A',2:'B'}
try:
    res=a/b
    print(res)
    #print(l[5])
    print(d[5])

except Exception as e:
  print(e,'unknown')


d={1:'A',2:'B'}
try:
    print(d[5])
except KeyError as e:
    print('Key Error')
else:
    print('Hello')
finally:
    print("Bye..")


try:
    print('Hi')
except Exception as e:
    print(e)
else:
    print('Hello')
    print('Hello')
finally:
    print('Bye..')

try:
    raise KeyError('hhhhhhhhhhhhhh')
except KeyError as e:
    print(e)




'''

# user defined exception
# class Myclass(Exception):
#     def _init_(self,msg):
#         super()._init_(msg)

# n=int(input("Value-"))

# if n<0:
#     try:
#         raise  Myclass('negative val:')
#     except Myclass as e:
#         print(e)
# else:
#     print('Value',n)


# d={1:'A',2:'B'}
# try:
#     print(d[1])
# except KeyError as e:
#     print('Key Error')
# else:
#     print('Hello')
# finally:
#     print("Bye..")

try:
    raise ZeroDivisionError('error......')
except ZeroDivisionError as e:
    print(e)