print("i hate you")


def swapCode(file1,file2,file3):
    with open(file1,"r") as a,open(file2,"r") as b, open(file3,"r") as c:
        c1=a.read()
        c2=b.read()
        c3=c.read()
    with open(file1,"w") as aa, open(file2,"w") as bb, open(file3,"w") as cc:
        cc.write(c1)
        bb.write(c3)
        aa.write(c2)
    
swapCode("b1.py","b2.py","b3.py")