# conditional statement
'''
a=10
b=20
if a>b:
    print('Hi')
    print('How are you?')
    print('Good')
else:
    print('Good morning')
    print('Bye')

v1=100
v2=200
if v1>v2:
    print('v1 is  greater')
else:
    print('v2 is  greater')

marks=int(input('Enter your Marks: '))
if marks>=90:
    print('Excellent')
elif marks<90 and marks>=80:
    print('Very Good')
elif marks<80 and marks>=70:
    print('Good')
else:
    print('Need Practice')

math=int(input("Enter Math Marks "))
phy=int(input("Enter Phy Marks "))
chem=int(input("Enter Chem Marks "))

avg=(math+phy+chem)/3
if avg>=90:
    print('Excellent:')
elif avg<90 and avg>=80:
    print('Very Good')
elif avg<80 and avg>=70:
    print('Good')
else:
    print('Need Practice:')

a=5
b=10
c=7

if a>b and a>c:
    print(a)
elif  b>c:
    print(b)
else:
    print(c)

if a>5:
    if b>10:
        if c>20:
            print('Hi')


bp=input('Enter Your Basic Pay:')

da
-------
if bp>50000=>da=10% of bp
if bp > 30000 and bp<=50 =>da=15% of bp
else da =>20 of bp


hra
----------
hra=15% of bp

gross salary=bp+da+hra

it calculation
-------------------
it= gross_sal >1L=>30 % of Gross salary
it =gross_sal>=50K and gross_sal<1L => 10% gross_sal
it=gross_sal<50k=>0


net_sal=gross_salary-it



a=100
if a>50:
    pass
else:
    print('Hi')




for i in range(1,11):
    print(i,'Nitin')
#for,while
'
for i in range(0,10,3):
    print(i)

for i in range(10,2,-1):
    print(i)

for i in range(3):
    for j in range(3):
        print((i,j),end=',')
    print()


#print odd no its sum from 1 to 100
s=0
for i in range(1,101):
    if i%2==1:
        print(i,end =' ')
        s+=i
print('\nsum of odd from 1 to 100',s)

#table of given

n=int(input('Enter any no:'))
for i in range(1,11):
    print('{} * {} = {}'.format(i,n,i*n))


i=0
while(i<10):
    print(i,end=' ')
    i=i+1
print()
for i in range(0,10):
    print(i,end=' ')


while True:
    print('Nitin:')
    choice=input('Do you want to continue press y:')
    if choice!='y':
        break

#continue,break and pass

for i in range(1,11):
    print(i)
    if i==5:
        break

for i in range(1,11):

    if i==5:
        continue
    print(i)

for i in range(1,11):
    pass
'''

#write a program to check given no is prime or not

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

