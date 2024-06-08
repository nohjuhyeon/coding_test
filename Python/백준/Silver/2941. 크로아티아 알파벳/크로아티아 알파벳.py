a = list(input())
for i in range(len(a)-2):
    if a[i] == "d" and a[i+1] == "z" and a[i+2] == "=":
        a[i] = 1
        a[i+1] = 2
        a[i+2] = 2
for i in range(len(a)-1):
    if a[i] == "c" and a[i+1] == "=":
        a[i] = 1
        a[i+1] = 2
        pass
    elif a[i] == "c" and a[i+1] == "-":
        a[i] = 1
        a[i+1] = 2
        pass
    elif a[i] == "d" and a[i+1] == "-":
        a[i] = 1
        a[i+1] = 2
    elif a[i] == "l" and a[i+1] == "j":
        a[i] = 1
        a[i+1] = 2
    elif a[i] == "n" and a[i+1] == "j":
        a[i] = 1
        a[i+1] = 2
    elif a[i] == "s" and a[i+1] == "=":
        a[i] = 1
        a[i+1] = 2
    elif a[i] == "z" and a[i+1] == "=":
        a[i] = 1
        a[i+1] = 2
    else:
        pass
for i in range(len(a)):
    if a[i] != 1 and a[i] != 2:
        if a[i] != "-" and a[i] != "=":
            a[i] = 1
print(a.count(1))
