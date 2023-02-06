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

#Arrange the array of indit of profit of products in descending order
Profit_index=[i for i in range(N)]
SortedProfit_index=sorted(Profit_index,key=lambda i:f[i],reverse=True)
MaxProfit=0
Answer=[0]*N
#Choose the best product
for i in SortedProfit_index:
    U=min(C//c[i],A//a[i])
    if U>=m[i]: 
        MaxProfit+=U*f[i]
        #Update
        C=C-c[i]*U
        A=A-a[i]*U
        Answer[i]+=U
        
print('Optimized Sotion is: ' + str(Answer))
print('With the profit is: ' + str(MaxProfit))
