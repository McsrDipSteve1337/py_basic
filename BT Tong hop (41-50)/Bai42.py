n=int(input())
ans=0
if(n<=1): ans=15
if(2<=n and n<=5): ans=12*(n-1)+15
if(n>=6): ans=10*(n-5)+63 
print(ans*1000)