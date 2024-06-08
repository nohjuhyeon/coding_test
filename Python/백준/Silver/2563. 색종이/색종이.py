count_set =set()
N = int(input())
for k in range(N):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            B = i+1+x,j+1+y
            count_set.add(B)
print(len(count_set))
