def maxmin(ds):
    minds=ds[0]
    maxds=ds[0]
    for i in range(len(ds)):
        minds=min(minds,ds[i])
        maxds=max(maxds,ds[i])
    return maxds,minds

def find(ds,x):
    for i in range(len(ds)):
        if(ds[i]==x): return i
    return "Khong tim thay"

def sortnb(ds):
    n=len(ds)
    for i in range(n):
        for j in range(n-i-1):
            if(ds[j]>ds[j+1]): ds[j],ds[j+1]=ds[j+1],ds[j]
    return ds

def sortchon(ds):
    n=len(ds)
    for i in range(n):
        minds=i
        for j in range(i+1,n):
            if(ds[minds]>ds[j]): minds=j 
        ds[i],ds[minds]=ds[minds],ds[i]
    return ds

n=int(input())
a=list(map(int,input().split()))
print(maxmin(a))
print(find(a,8))
print(sortnb(a))
print(sortchon(a))