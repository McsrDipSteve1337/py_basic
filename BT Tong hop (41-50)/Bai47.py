m,y=map(int,input().split())
if((m<8 and m%2==1) or (8<=m<=12 and m%2==0)): print(31)
elif(m==2):
    if(y%400==0 or(y%4==0 and y%100!=0)): print(29)
    else: print(28)
else: print(30)