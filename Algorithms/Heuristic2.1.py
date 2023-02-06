with open("test.txt", "r") as f:
    Firstline=f.readline()
    Secondline=f.readline()
    Thirdline=f.readline()
    Fourthline=f.readline()
    Fifthline=f.readline()
N,A,C=list(map(int,Firstline.split()))
c=list(map(int,Secondline.split()))
a=list(map(int,Thirdline.split()))
f=list(map(int,Fourthline.split()))
m=list(map(int,Fifthline.split()))

check=[True]*N
MaxProfit=0
Answer=[0]*N
while sum(check) and (N>0):
    Profit=[0]*N
    k=0
    for i in range(N):
        if check[i]==True:
            U=min(C//c[i],A//a[i])
            if U<m[i]:
                check[i]=False
            else:
                Profit[i]=U*f[i]
                k+=1
    if k==0:
        break
    index=Profit.index(max(Profit))
    C=C-c[index]*m[index]
    A=A-a[index]*m[index]
    Answer[index]+=m[index]
    MaxProfit+=f[index]*m[index]
    m[index]=1

print('Optimized Sotion is: ' + str(Answer))
print('With the profit is: ' + str(MaxProfit))    
