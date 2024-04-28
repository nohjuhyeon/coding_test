import sys
A = int(input())
E = 0
for D in range(A):
    B, C = map(int, sys.stdin.readline() .split())
    E = E + 1
    D = B + C 
    print("Case #{}: {} + {} = {}".format(E,B,C,D))