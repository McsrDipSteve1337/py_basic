a,b,c=map(float,input().split())
yes="Hop le"
no="Khong hop le"
if(a<0 or b<0 or c<0):
    print(no)
elif(a+b>c or a+c>b or b+c>a):
    print(yes)
else:
    print(no)