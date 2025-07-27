ds=[]
def addhs(ds,name,age,score):
    hs={
        "name":name,
        "age":age,
        "score":score
    }
    ds.append(hs)
    
def findhs(ds,name:str):
    for hs in ds:
        if hs["name"]==name: return hs
        
def sap_xep_theo_diem(ds):
    ds.sort(key=lambda hs: hs["diem"], reverse=True)

def xeploai(score:int):
    if(score>=9): print("Xuất sắc")
    elif(score>=8): print("Giỏi")
    elif(score>=6.5): print("Khá")
    elif(score>=5): print("Trung bình")
    else: print("Yếu")

def thong_ke(ds):
    so_hs=len(ds)
    
    dtb=0
    for i in ds:
        dtb+=i["score"]
    dtb/=so_hs
    
    ds=sap_xep_theo_diem(ds)
    best=ds[1]
    worst=ds[-1]
    
    xep_loai={}
    for hs in ds:
        xl=xeploai(hs["score"])
        if(xl in xep_loai): xep_loai[xl]+=1
        else: xep_loai[xl]=1
        
    return {
        "Tổng số học sinh": so_hs,
        "Điểm trung bình lớp": round(dtb,2),
        "Xếp loại": xep_loai,
        "Học sinh giỏi nhất": {
            "Tên": best["name"],
            "Điểm": best["score"],
        },
    }
    
