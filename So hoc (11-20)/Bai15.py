def snt(n:int)->bool:
    if(n<2):
        return False
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True

n=int(input())
if(snt(n)):
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")