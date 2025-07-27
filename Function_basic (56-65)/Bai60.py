def dem_tu(s:str)->int:
    a=list(s.split())
    return len(a)

def dao_chuoi(s:str)->str:
    return s[::-1]

def ispalindrome(s:str)->bool:
    sdx=dao_chuoi(s)
    return sdx==s

def chuan_hoa(s:str)->str:
    ns=list(s.split())
    res=""
    for i in ns:
        i=i.capitalize()
        res=res+i+' '
    return res[:-1]
n=input()
print(f"So tu: {dem_tu(n)}")
print(f"Chuoi dao nguoc: {dao_chuoi(n)}")
print(ispalindrome(n))
print(chuan_hoa(n))