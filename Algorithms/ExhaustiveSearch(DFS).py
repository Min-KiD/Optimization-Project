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

n = [0] * N

maxx = 0
maxL = n
ind = 0

def sumFast(a, b):
    return sum([i*j for i,j in zip(a,b)])

def BT(ind, n, N):
    global A, C, c, a, f, m, maxx, maxL
    if N < 1:
        return 
    for i in range(min(A//a[ind], C//c[ind]) + 1):
        if i < m[ind] and i != 0:
            continue
        V = n.copy()
        V[ind] = i  
        if sumFast(c, V) <= C and sumFast(a, V) <= A:
            if sumFast(f, V) >= maxx:
                maxx = sumFast(f, V)
                maxL = V.copy()
        BT(ind+1, V, N-1)
        
BT(ind, n, N)

print('Optimized Sotion is: ' + str(maxL))
print('With the profit is: ' + str(maxx))
