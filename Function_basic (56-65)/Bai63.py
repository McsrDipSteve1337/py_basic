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

    