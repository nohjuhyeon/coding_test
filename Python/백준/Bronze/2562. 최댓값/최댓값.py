list_i = []
for i in range(9):
    list_i.append(int(input()))
    pass

print(max(list_i))
x = list_i.index(max(list_i)) + 1
print(x)                  