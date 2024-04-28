A = int(input())
b = 0

for a in range(A):
    b = b + 1
    a = A - b
    x = 0
    y = 0
    c = ""
    d = ""
    while x < b:
        x =x + 1
        c = "*{}".format(c)
        pass
    while y < a:
        y = y + 1
        d = " {}".format(d)
        pass    
    print("{}{}".format(d,c))
