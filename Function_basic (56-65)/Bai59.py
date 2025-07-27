def Shv(a:int):
    if(a<=0): return "Loi: Canh hinh vuong phai duong"
    return a**2
def Shcn(a,b):
    if(a<=0 or b<=0):
        return "Loi: Canh hinh chu nhat phai duong"
    return a*b
def Sht(r:int):
    if(r<=0): return "Loi: Ban kinh phai duong"
    return r*r*3.14159
def Stg(a,b,c):
    if(a<=0 or b<=0 or c<=0): return "Loi: Canh tam giac phai duong"
    if(a+b>c and a+c>b and b+c>a):
        p=(a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c))**0.5
    else: return "Loi: Khong phai ba canh cua mot tam giac"

def xuly():
    s=input("Chon hinh muon tinh dien tich (vuong,chu nhat,tron,tam giac): ")
    if(s=="vuong"):
        a=int(input("Nhap so do canh: "))
        print(Shv(a))
    elif(s=="chu nhat"):
        a,b=map(int,input("Nhap chieu dai, chieu rong: ").split())
        print(Shcn(a,b))
    elif(s=='tron'):
        r=int(input("Nhap ban kinh: "))
        print(Sht(r))
    else:
        a,b,c=map(int,input("Nhap so do 3 canh: ").split())
        print(Stg(a,b,c))

xuly()
