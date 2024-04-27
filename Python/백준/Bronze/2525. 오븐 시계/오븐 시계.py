a,b = map(int, input().split())
c = int(input())
if a + int((b + c)/60) < 24:
    print("{} {}".format(a + int((b + c)/60), (b + c)% 60))
    pass
else : 
    print("{} {}".format(a + int((b + c)/60)-24, (b + c)% 60))
