A,B = input().split()
list_a=[]
def print_max(C):
    for i in range(len(C)):
        list_a.append(C[i])
        pass
    list_a.reverse()
    for i in range(len(C)):
        print(list_a[i], end ="")
        pass
    print("")


    
if A[2] == B[2]:
    if A[1] ==B[1]:
        if A[0] > B[0]:
            C = A
            print_max(C)
            pass
        else:
            C = B
            print_max(C)
            pass
        pass
    elif A[1] > B[1]:
        C = A
        print_max(C)
        pass
    else:
        C = B
        print_max(C)
        pass
    pass
elif A[2] > B[2]:
    C = A
    print_max(C)
    pass
else:
    C = B
    print_max(C)
