n=int(input())
a=list(map(float,input().split()))
res=0
for i in a:
    res+=i
res/=n
print(f"Diem TB: {res}, Xep loai: ",end='')
if(res>=9): print("Xuất sắc")
elif(res>=8): print("Giỏi")
elif(res>=6.5): print("Khá")
elif(res>=5): print("Trung bình")
else: print("Yếu")