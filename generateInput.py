import random as rd
def make_testset():
    g=open("d:/New folder/test.txt",'w')
    N=rd.randint(1,1000)
    A=rd.randint(1,100)
    C=rd.randint(1,100)
    c=[str(rd.randint(1,100)) for i in range(N)]
    a=[str(rd.randint(1,100)) for i in range(N)]
    f=[str(rd.randint(1,100)) for i in range(N)]
    m=[str(rd.randint(1,100)) for i in range(N)]
    g.writelines(str(N)+' '+str(A)+' '+str(C)+'\n')
    g.writelines(str(i)+' ' for i in c)
    g.writelines('\n')
    g.writelines(str(i)+' ' for i in a)
    g.writelines('\n')
    g.writelines(str(i)+' ' for i in f)
    g.writelines('\n')
    g.writelines(str(i)+' ' for i in m)
    g.writelines('\n')   
    g.close()
make_testset()
g=open("d:/New folder/test.txt",'r')
print(g.read())
g.close()
