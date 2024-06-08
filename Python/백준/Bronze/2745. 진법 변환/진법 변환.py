n,b = input().split() 

def quest(n,b):
    answer = 0
    b = int(b)
    n = list(n)
    list_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(len(n)):
        if n[i] in list_alphabet:
            n[i] = list_alphabet.index(n[i])+10
        else:
            n[i] = int(n[i])
    for i in range(len(n)):
        answer += b**(len(n)-i-1)*n[i]
    return answer

answer = quest(n,b)
print(answer)