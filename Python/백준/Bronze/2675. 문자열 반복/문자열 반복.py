T = int(input())
for a in range(T):
    R,S = input().split()
    list_a = []
    for b in range(len(S)):
        for c in range(int(R)):
            print("{}".format(S[b]), end = "")
    print("")