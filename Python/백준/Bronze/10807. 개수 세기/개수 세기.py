def count():
    num_input = int(input())
    list_input = list(input().split())
    num_check = input()
    num_count = 0
    for i in range(num_input):
        if num_check == list_input[i]:
            num_count += 1
    print(num_count)


count()