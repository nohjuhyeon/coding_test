N = int(input())
output = 0
for i in range(N):
    str_word = list(input())
    alphabet_list = list(set(str_word))
    check = 1
    for j in range(len(alphabet_list)):
        alphabet_count = str_word.count(alphabet_list[j])
        alphabet_index = str_word.index(alphabet_list[j])
        for k in range(alphabet_count):
            if str_word[alphabet_index] == str_word[alphabet_index + k]:
                check = check * 1
                pass
            else:
                check = 0
    if check == 1:
        output = output + 1
        pass
print(output)
