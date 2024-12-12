def solution(wallet, bill):
    answer = 0
    wallet = sorted(wallet)
    bill = sorted(bill)
    while True:
        if wallet[0] >= bill[0] and wallet[1] >= bill[1]:
            break
        else:
            new_bill = bill
            if bill[0] > bill[1]:
                new_bill[0] = bill[0]//2
            else:
                new_bill[1] = bill[1]//2
            answer+= 1
            bill = new_bill
            bill = sorted(bill)
    return answer