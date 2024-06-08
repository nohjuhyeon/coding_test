N, B = map(int,input().split())

def question(N,B):
    list_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    M=[]
    while True:

        if int(N%B) >= 10: 
            M.append(list_alphabet[int(N%B)-10])
        else:
            M.append(int(N%B))
        if N < B:
            # if int(N) >= 10: 
            #     M.append(list_alphabet[N-10])
            # else:
            #     M.append(N)
            break
        N =int(N/B)
    
    for i in range(len(M)):
        print(M[len(M)-i-1],end='')
    print("")
    return 0
answer = question(N,B)
