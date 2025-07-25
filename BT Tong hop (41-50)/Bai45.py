def ucln(a,b)->int:
    while(b!=0):
        a,b=b,a%b
    return a

a,b=map(int,input().split())
print(f"UCLN: {ucln(a,b)}, BCNN: {a//ucln(a,b)*b}")