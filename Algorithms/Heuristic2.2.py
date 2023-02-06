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
            if U<m[i]:
                check[i]=False
            else:
                Profit[i]=U*f[i]
                k+=1         
    if k==0:
        break   
    index=Profit.index(max(Profit))
    U=min(C//c[index],A//a[index])
    X=(U+m[index])//2
    C=C-c[index]*X
    A=A-a[index]*X
    Answer[index]+=X
    MaxProfit+=f[index]*X
    
print('Optimized Sotion is: ' + str(Answer))
print('With the profit is: ' + str(MaxProfit)) 
