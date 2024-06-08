def question():
    while True:
        list_A = list(map(int,input().split()))
        if list_A[0] == 0 and list_A[1] == 0 and list_A[2] == 0:
            break
        else:
            list_A=sorted(list_A)
            if list_A[2] >= list_A[0] + list_A[1]:
                print("Invalid")
            else:
                list_A = list(set(list_A))
                if len(list_A) == 3:
                    print("Scalene")
                elif len(list_A) == 2:
                    print("Isosceles")
                else:
                    print("Equilateral")

question()