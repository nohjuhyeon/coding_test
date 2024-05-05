list_a = []
list_b = []
for i in range(10):
    b = int(input())%42
    list_a.append(b)
    pass

for i in range(10):
    d =0
    for j in range(i,10):
        if list_a[j] == list_a[i]:
            d = d + 1
        pass
    list_b.append(d)
    pass
pass
x = list_b.count(1)
pass
print(x)