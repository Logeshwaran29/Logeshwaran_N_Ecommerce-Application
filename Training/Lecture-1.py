#print("Hello welcome to python programming:")
'''
var_a=10
var_b=20
sum=var_a+var_b
print('Sum is ',sum)

sub=var_a-var_b
print('Sub is ',sub)

mul=var_a*var_b
print('Mul is ',mul)

div=100/3
print('Float div ',div)

intdiv=100//3
print('Int div ',intdiv)

moddiv=100%3
print('Mod div ',moddiv)

expn=100**2
print('Mod div ',expn)
#(+,-,*,/,//,%,**) arithmetic operators

a=10
b=20
print(a>=b)
print(a<b)
print(a!=b)
print(a==b)

a=True
b=False
print(a and b)

a=True
b=True
print(a and b)

a=False
b=False
print(a and b)

a=False
b=True
print(a and b)



a=True
b=False
print(a or b)

a=True
b=True
print(a or b)

a=False
b=False
print(a or b)

a=False
b=True
print(a or b)

a=False
b=True
print( not (a or b))
# (and,or,not)

a=10
b=10.5
c=True
d='Amit'
e=10+20j

print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))

a=10
b=10
print(a is b)
city='Delhi'
print('D' in city)


# string
s1="Hexaware"
print(s1[0])
print(s1[1])
#s1[0]='J'

print(s1*2)
print(s1+'Technology')

print(type(s))
a='100'
for i in a:
    print(i)
# string:seguence,imutable,index,*,+ used with str,'',"",''' ''',iterate with loop

# list

l1=[1,2,3,4,5,6,6,5]
print(l1)
l=[10,20.5,True,'Amit']
print(l)
l=[10,20,[1,2,3,4,5],30,50]
print(l[2][-1])
print(l[-3][-3])
print(l1*2) # repeatation
print(l1+l) #concat
l1=[1,2,3,4,5,6,6,5]
l1[0]=100 #mutable
for i in l1:
    print(i)

# propertis of List
#1. index used
#2. disimilar data
#3. iterate with loop
#4. duplicate allow
#5. mutable
#6. ordered

l1=[10,20,30,40,50,10.5,10,20]
l2=[100,200,300]
#l1.extend(l2)#add the l2 in l1
#l1.append('Amit')
#l3=l1.copy()
print(l1.count(10))
print(l1.index(10))
l1.insert(0,100)
print(l1)
print(l1.pop())
print(l1)
l1.remove(10)
print(l1)
l1.reverse()
print(l1)
l1.sort()
print(l1)


l1=[10,20,30,10,40,50,50,20]
l2=[]
for i in l1:
    if l1.count(i)>1 and i  not in l2:
        l2.append(i)
print(l2)

# max and min element in the list
l1.sort()
print(l1[-1],l1[0])
print(max(l1),min(l1))

#tuple
t=(10,10,20,30,40,50,50,10.5,'python')
print(t[0])
print(t)
#t[0]=100
for i in t:
    print(i)

#tuple
=======
1. index used 
2. disimilar data
3. iterate with loop
4. duplicate allow
5. immutable
6. ordered

t=(10,10,20,30,40,50,50,10.5,'python')
for i in dir(t):
    print(i)


s={10,2,3,4,4} #set
print(s)
#print(s[0])
for i in s:
    print(i)
set  
1. disimilar data
2. iterate with loop
3. mutable
4. unordered

s={1,2,10.5}
s.add(100)
print(s)


s=set()
print(type(s))


#dict

print(student)
print(student[102])
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

student={101:'amit',102:'sumit',103:'somya',104:'rajnikant',}
for k,v in student.items():
    if v[0]=='s':
        print(k,v)

l=[1,1,1,3,3,4,5,5,6,7,7]
#d[1:3,3:2,4:1,5:2,6:1,7:2]
d={}
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)


# properties of dict
#1. no index allowed
#2. duplicate allowed in values
#3. oredered
#4. key and values pair
#5. iterate with loop
#6. mutable

d.keys()#return the all the keys
d.values()#return the all values
d.items()#return the key and value in pair
d.clear()#delete all key and values
d.get(101)#return the values
d.update({106:'Likitha'})#add the pair in the dict
d.pop(99)#delete the given key from the dict
d.popitem()#delete the last pair from dict

'''

l=[1,2,3,4,5]
t=tuple(l)
print(type(t))
l=[1,1,2,3,4,4]
print(set(l))

#function of set with one example







