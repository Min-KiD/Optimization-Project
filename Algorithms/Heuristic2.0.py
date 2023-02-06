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
while sum(check):
    Profit=[0]*N
    k=0
    for i in range(N):
        if check[i]==True:
            U=min(C//c[i],A//a[i])
            if U>=m[i] :
                Profit[i]=U*f[i]
                k+=1
            else:
                check[i]=False
    if k==0:
        break
    index=Profit.index(max(Profit))
    U=int(min(C/c[index],A/a[index]))
    C=C-c[index]*U
    A=A-a[index]*U
    Answer[index]+=U
    MaxProfit+=max(Profit)
    
print('Optimized Sotion is: ' + str(Answer))
print('With the profit is: ' + str(MaxProfit))
