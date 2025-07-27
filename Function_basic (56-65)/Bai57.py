def giai_thua(n:int)->int:
    if(n<2): return 1
    ans=1
    for i in range(2,n+1): ans*=i
    return ans

n=int(input())
print(giai_thua(n))