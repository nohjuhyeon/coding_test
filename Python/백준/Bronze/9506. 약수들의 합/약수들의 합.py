def question():
    while True:
        n = int(input())
        if n == -1:
            break
        else:
            answer_list = []
            for i in range(n-1):
                if n%(i+1) == 0:
                    answer_list.append(i+1)
        if sum(answer_list) == n:
            for i in range(len(answer_list)):
                answer_list[i] = str(answer_list[i])
            answer = " + ".join(answer_list)
            print("{} = {}".format(n,answer))
        else:
            print("{} is NOT perfect.".format(n))

question()