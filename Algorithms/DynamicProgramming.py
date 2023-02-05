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

def DP(N, m, n):
    global c, a, A, C, f, K
    if N <= 0:
        return 0
    
    V = n.copy()
    V[N-1] = m[N-1] 
    M = m.copy()
    M[N-1] += 1

    if sumFast(a, V) > A or sumFast(c, V) > C:
        T = V.copy()
        T[N-1] -=1
        K.append(T)
        return DP(N-1, M, n)
    
    return max(f[N-1]*V[N-1] + DP(N-1, m, V), DP(N, M, n))

def sumFast(a, b):
    return sum([i*j for i,j in zip(a,b)])

K = []

maxx = DP(N, m, n)
maxL = K[0]
for i in K:
    if sumFast(f, i) == maxx and sumFast(a, i) <= A and sumFast(c, i) <= C:
        maxL = i
        
print('Optimized Sotion is: ' + str(maxL))
print('With the profit is: ' + str(maxx))
