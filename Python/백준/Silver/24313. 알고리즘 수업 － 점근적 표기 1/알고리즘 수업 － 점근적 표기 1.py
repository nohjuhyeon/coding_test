a,b = map(int,input().split())
c = int(input())
d = int(input())
def question(a,b,c,d):
    if a>c:
        print(0)
    else:
        if a*d+b<=c*d:
            print(1)
        else:
            print(0)
answer = question(a,b,c,d)