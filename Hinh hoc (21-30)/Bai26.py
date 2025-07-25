def pytago(a,b,c)->bool:
    if(a**2+b**2==c**2 or a**2+c**2==b**2 or c**2+b**2==a**2):
        return True
    else:
        return False
def istg(a,b,c)->bool:
    if(a<0 or b<0 or c<0):
        return False
    elif(a+b>c or a+c>b or b+c>a):
        return True
    else:
        return False
a,b,c=map(float,input().split())
if(istg(a,b,c)):
    if(a==b and b==c):
        print("Tam giac deu")
    elif(pytago(a,b,c)):
        if(a==b or b==c or a==c):
            print("Tam giac vuong can")
        else:
            print("Tam giac vuong")
    elif(a==b or b==c or c==a):
        print("Tam giac can")
    else:
        print("Tam giac thuong")
else:
    print("Khong phai 3 canh cua mot tam giac")