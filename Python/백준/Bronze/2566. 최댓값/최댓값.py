list_input = []

for i in range(9):
    list_input.extend(map(int, input().split()))

print(max(list_input))
row = int((list_input.index(max(list_input)))/9 + 1)
column = (list_input.index(max(list_input)))%9 + 1
print("{} {}".format(row, column))