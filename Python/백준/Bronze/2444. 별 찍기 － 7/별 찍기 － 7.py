N = int(input())
repeat = (N * 2) - 1
# N = 1 - 1 1 
# N = 2 - 3 1 3 1
# N = 3 - 5 1 3 5 3 1 
# N = 4 - 7 1 3 5 7 5 3 1

for i in range(N):
    for j in range(N-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print("")
for i in range(N-1):
    for j in range(i+1):
        print(" ", end="")
    for j in range((2*N - 3) -2*i):
        print("*",end="")
    print("")