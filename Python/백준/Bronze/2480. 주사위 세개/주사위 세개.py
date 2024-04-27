class Quest:
    def __init__(self):
        self.input_dice = list(map(int,input().split()))
        self.dice_first = self.input_dice[0]
        self.dice_second = self.input_dice[1]
        self.dice_third = self.input_dice[2]

    def check(self):
        if self.dice_first == self.dice_second == self.dice_third:
            check = 3
            list_check = self.dice_first
        elif self.dice_first == self.dice_second:
            check = 2
            list_check =self.dice_first
        elif self.dice_first == self.dice_third:
            check = 2
            list_check = self.dice_first
        elif self.dice_second == self.dice_third:
            check = 2
            list_check = self.dice_second
        else:
            check = 1
            list_check = max(self.dice_first,self.dice_second,self.dice_third)
        return check,list_check
    
    def price(self,check,list_check):
        if check == 1:
            print(list_check * 100)
        elif check == 2:
            print(list_check * 100 + 1000)
        elif check == 3:
            print(list_check * 1000 + 10000)

quest = Quest()
check,list_check = quest.check()
pass
quest.price(check,list_check)
pass

