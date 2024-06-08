import sys
n = int(sys.stdin.readline().rstrip())

def question(n):
    input_list = list(map(int,sys.stdin.readline().rstrip().split()))
    extra_list = []
    answer_list = []
    answer = 'Nice'
    for i in range(1,n+1):
        while True:
            if len(input_list) == 0 and extra_list[-1] !=i:
                answer = 'Sad'
                break
            elif len(input_list) != 0 and input_list[0] == i:
                answer_list.append(i)
                input_list.pop(0)
                break
            elif len(extra_list) !=0:
                if extra_list[-1] == i:
                    answer_list.append(i)
                    extra_list.pop()
                    break
                else:
                    extra_list.append(input_list[0])
                    input_list.pop(0)
            else:
                extra_list.append(input_list[0])
                input_list.pop(0)

    return answer

answer = question(n)
print(answer)