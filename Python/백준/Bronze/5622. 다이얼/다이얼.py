list_number = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

tele_input = input()
tele_output = 0
pass
for i in range(len(tele_input)):
    if list_number.index(tele_input[i]) <= 2:
        tele_output = 3 + tele_output
        pass
    elif list_number.index(tele_input[i]) <= 5:
        tele_output = 4  + tele_output
        pass
    elif list_number.index(tele_input[i]) <= 8:
        tele_output = 5  + tele_output
        pass
    elif list_number.index(tele_input[i]) <= 11:
        tele_output = 6  + tele_output
        pass
    elif list_number.index(tele_input[i]) <= 14:
        tele_output = 7  + tele_output
        pass
    elif list_number.index(tele_input[i]) <= 18:
        tele_output = 8  + tele_output
        pass
    elif list_number.index(tele_input[i]) <= 21:
        tele_output = 9  + tele_output
        pass
    elif list_number.index(tele_input[i]) <= 25:
        tele_output = 10  + tele_output
        pass
    pass
pass
print(tele_output)