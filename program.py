def binary(l1):
    l=[];b=""
    for i in l1:
        k=i.split('.')
        for j in k:
            bi=bin(int(j))[2:];bi="0"*(8-len(bi))+bi+"."
            b+=bi 
        b+=' '
    b=b[:-1]
    b=b.split(' ')
    b[-1]=b[-1][:-1]
    return b 
def hexadecimal(l1):
    l=[]
    b=""
    for i in l1:
        k=i.split('.')
        for j in k:
            bi=hex(int(j))[2:];bi="0"*(2-len(bi))+bi+"."
            b+=bi
        b+=' '
    b=b[:-1]
    b=b.split(' ')
    b[-1]=b[-1][:-1]
    l.append(b)
    return b 
def octal(l1):
    l=[];b=""
    for i in l1:
        k=i.split('.')
        for j in k:
            bi=oct(int(j))[2:];bi="0"*(4-len(bi))+bi+"."
            b+=bi
        b+=' '
    b=b[:-1]
    b=b.split(' ')
    b[-1]=b[-1][:-1]
    l.append(b)
    return b 
def get_ip(string):
    addr=list(map(str,string.split('.')))
    if len(addr)!=4:
        return 0 
    for val in addr:
        if not val.isnumeric():
            return 0
        else:
            val=int(val)
        if val not in range(0,256):
            return 0
    return '.'.join([elem for elem in addr])
import pickle
l=[];ok=["first","second","third","fourth","fifth","sixth","seventh","eigth","ninth","tenth"];ind=[]
for i in range(10):
 string=input().strip()
 ip=get_ip(string)
 if(ip) and (not(i in l)):
    l.append(string)
    ind.append(i)
 else:
    print("invalid ip address")
l1=binary(l)
l2=hexadecimal(l)
l3=octal(l)
with open('conversion.txt', 'wb') as fp:
 pickle.dump(binary(l), fp)
 pickle.dump(hexadecimal(l),fp)
 pickle.dump(octal(l),fp)
with open ('conversion.txt', 'rb') as fp:
 itemlist1 = pickle.load(fp)
 itemlist2 = pickle.load(fp)
 itemlist3 = pickle.load(fp)
k=0
print(len(l1))
for i in range(len(l1)):
 print("The "+ok[ind[i]]+" IP address in Decimal,Binary,Octal and hexadecimal format is ",end="")
 print(l1[i],l2[i],l3[i],sep=", ")
