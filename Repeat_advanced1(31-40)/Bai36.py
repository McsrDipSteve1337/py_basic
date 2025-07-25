a,n=map(int,input().split())
ans=a
for i in range(2,n+1):
    ans*=a
print(ans)