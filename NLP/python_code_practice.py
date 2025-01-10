# no amstrong or not

armstrong=123
armstrong=(int(armstrong))

y=[int(x)for x in str(armstrong)]

d=sum(y)
if d== armstrong:
    print("true")
else:
    print("False")

    # no is prime or not 
def prme(n):
    if n <= 1:
        return True
    for i in range(2, int( n//2)):
        if n % i ==0:
            return False
        
    return True
if prme(7) == True:
    print("number is  is prime")
else:
    print("not prime")

#Fibonaccie series.

# 0,1,(n-1)+(n-2)


def fab(n):
    f=[0,1]
    for i in range(2, n):
        nextno=f[-1]+f[-2]
        f.append(nextno)
    return f
n=10
print(fab(n))


n=("abb")
m=n[::-1]

if n==m : 
    print("this is palandrom",n)
else:
    print("not palendrom ", n)

a=list(map(int,input("enter the value").split()))
print("lsit no",a)

a,b,c=input()
print(a)    
print(b)
print(c)