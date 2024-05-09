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
# print(obj1.c)
# print(obj2.c)
# print(obj3.c)


# Inheritance:

# class X:
#     def _init_(self):
#         self.a=100
#     def fun(self):
#         print(self.a)
# class Y(X):
#     def _init_(self):
#         super()._init_()
#         self.b=200

#     def foo(self):
#         print(f'b= {self.b}, a= {self.a}')
# obj=Y()
# obj.foo()
#obj.fun()


# class x:
#     def _init_(self):
#         print('welcome to x class')
#     def x_fun(self):
#         print('welcome x function')
# class y():
#     def  _init_(self):
#         super()._init_()
#         print('welcome to y class')
#     def y_fun(self):
#         print('welcome y function')
# class z(x,y):
#     def  _init_(self):
#         super()._init_()
#         super(x,self)._init_()
#         print('welcome to z class')
#     def z_fun(self):
#         print('welcome z function')

# obj=z()
# obj.z_fun()
# obj.y_fun()
# obj.x_fun()

# Types: single,multiple,multilevel,heirarchical


# class X:
#     pass
# class Y(X):
#     pass
# class Z(Y):
#     pass

# class X:
#     pass
# class Y(X):
#     pass
# class Z(X):
#     pass


# data overriding
# class X:
#     def _init_(self):
#         self.a=100

# class Y(X):
#     def _init_(self):
#         self.a=200
#     def show(self):
#         print(self.a)#derived class variable
#         print(X().a)#base class variable
# obj=Y()
# obj.show()


# class X:
#     def _init_(self):
#         self.a=100
#     def show(self):
#         print('X show')
# class Y(X):
#     def _init_(self):
#         super()._init_()
#         self.a=200
#     def show(self):
#         X.show(self)
#         print(X().a)
#         print(self.a)
# obj=Y()
# obj.show()

'''

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
'''