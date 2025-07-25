n=int(input())
s=""
while(n!=0):
    p=n%2
    s=str(p)+s
    n//=2
print(s)