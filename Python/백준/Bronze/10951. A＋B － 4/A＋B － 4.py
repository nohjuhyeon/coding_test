A,B = map(int, input().split())        
while True:
    try:
        print(A + B)
        A,B = map(int, input().split())
    except:
        break
