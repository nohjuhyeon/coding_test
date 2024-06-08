a,b,c,d,e,f = map(int,input().split())

def question(a,b,c,d,e,f):
    if a == 0:
        y = int(c/b)
        x = int((f-e*y)/d)
    elif b == 0:
        x = int(c/a)
        y = int((f-d*x)/e)
    elif d == 0:
        y = int(f/e)
        x = int((c-b*y)/a)
    elif e == 0:
        x = int(f/d)
        y = int((c-a*x)/b)
    else:
        x = int((f*b-c*e)/(d*b-a*e))
        y = int((c-x*a)/b)
    answer = [x,y]

    return answer

answer = question(a,b,c,d,e,f)
print(*answer)
