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

#variable in the class:instance variable,class,private and protected
# class X:
#     c=0

#     def _init_(self):
#         self.a=0
#         self.b=0
#         self.__pri=100
#         self._pro=200
#     def show(self):
#         print(X.c)
#         print(self.a)
#         print(self.b)
#         #print(self.__pri)
#         #print(self._pro)
# obj=X()
# #obj.show()
# print(X.c)
# print(obj.a)
# print(obj.b)
# #print(obj.__pri)
# #print(obj._pro)
