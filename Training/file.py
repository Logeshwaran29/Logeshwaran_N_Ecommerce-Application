# f=open("sample.txt","w")
#
# d="Enjoy technical deep dives, one on one expert advice, product announcements, and more.\nJoin us for a day-long event to elevate your skills."
# f.write(d)
# f.close()

# f=open("sample.txt",'r')
# s=0
# for i in f:
#     s+=1
# print('No of lines:',s)
#
# a=f.read().split(' ')
# print('No of words:',len(a))

# read character by character
# c1=0
# while 1:
#     c=f.read(1)
#     if not c: break
#     print(c,end="")
#     c1+=1
#
# print('\n',c1)

# a=f.read().split(' ')
# print(a)
# b,c=input(),0
# for i in a:
#     if b == i: c+=1
# print(b,":",c)


class fileNotFound(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message

# try:
#     try:
#         f = open("sample1.txt", 'r')
#         print(f.read())
#     except Exception as e:
#         raise fileNotFound('File not found...')
# except Exception as e:
#     print(e)


try:
    f = open("sample1.txt", 'r')
    a = f.read()
    if len(a) < 1:
        raise fileNotFound('File not found....')
    else:
        print(a)
except Exception as e:
    print(e)
