def snt(n:int)->bool:
    if(n<2): return False
    for i in range(2,n):
        if(n%i==0): return False
    return True

n=int(input())
for i in range(2,n+1):
    if(snt(i)): print(i,end=' ')