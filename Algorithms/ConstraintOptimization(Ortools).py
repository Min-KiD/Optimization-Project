from ortools.sat.python import cp_model

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

model = cp_model.CpModel()

# Creates the variables.
for i in range(N):
    n[i] = model.NewIntVarFromDomain(cp_model.Domain.FromIntervals([[0],[m[i], 9999999]]), 'n'+str(i))

# Creates the constraints.
model.Add(sum(a[i]*n[i] for i in range(N)) <= A)
model.Add(sum(c[i]*n[i] for i in range(N)) <= C)

model.Maximize(sum(f[i]*n[i] for i in range(N)))

# Creates a solver and solves the model.
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print('Optimized Sotion is: ' + str(list(solver.Value(n[i]) for i in range(N))))
    print(f'With the profit is: {solver.ObjectiveValue()}')
else:
    print('No solution found.')
