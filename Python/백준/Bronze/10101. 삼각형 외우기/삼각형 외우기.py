def question():
    list_answer = []
    for i in range(3):
        list_answer.append(int(input()))
    if sum(list_answer) != 180:
        print("Error")
    else:
        set_answer = list(set(list_answer))
        if len(set_answer) == 1:
            print("Equilateral")
        elif len(set_answer) == 2:
            print("Isosceles")
        else:
            print("Scalene")

question()