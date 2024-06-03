def str_index_find(str_input):
    index = int(input()) - 1
    str_index = str_input[index]
    return str_index

str_input = input()
str_index = str_index_find(str_input)
print(str_index)