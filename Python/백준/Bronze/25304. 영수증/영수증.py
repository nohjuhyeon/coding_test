X = int(input())
N = int(input())
Y = 0
D = 0
while Y < N:
    Y = Y + 1
    A,B = map(int, input() .split())
    C = A * B
    D += C
    if Y >= N:
        pass
if X == D:
    print("Yes")
else:
    print("No")