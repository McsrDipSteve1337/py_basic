def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n - 1) + fibonacci(n - 2)

def luy(a,n):
    if n==0: return 1
    else: return a*luy(a,n-1)
    
def dao_nguoc(s):
    if len(s) <= 1: return s
    return dao_nguoc(s[1:]) + s[0]

def gcd(a,b):
    if b==0: return a
    else: return gcd(b,a%b)
    
n=int(input("Nhập số n: "))
print(f"Số fibonacci thứ {n} là: {fibonacci(n)}")
a,b=map(int,input("Nhập cơ số và mũ của luỹ thừa: ").split())
print(luy(a,b))
s=input("Nhập chuỗi cần đảo ngược: ")
print(dao_nguoc(s))
c,d=map(int,input("Nhập vào hai số a,b: ").split())
print(f"Ước chung lớn nhất của hai số là: {gcd(c,d)}")