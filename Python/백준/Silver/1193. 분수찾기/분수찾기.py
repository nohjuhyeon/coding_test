n = int(input())

def question(n):
    a = 0
    b= 0
    while True:
        a +=b
        b +=1
        if n <= a+b:
            break
    if int(b%2)==0:
        answer = "{}/{}".format(n-a,b+1-n+a)
    else:
        answer = "{}/{}".format(b+1-n+a,n-a)  
    return answer
answer = question(n)
print(answer)