n=int(input())
a=0
b=1
print(0,end=' ')
for i in range(n-1):
    a,b=b,a+b
    print(a,end=' ')