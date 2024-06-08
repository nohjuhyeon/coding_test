def question():
    input_list = []
    for i in range(5):
        input_list.append(int(input()))
    input_list = sorted(input_list)
    average_num = int(sum(input_list)/len(input_list))
    median_num = input_list[int(len(input_list)/2)]
    print(average_num)
    print(median_num)

question()