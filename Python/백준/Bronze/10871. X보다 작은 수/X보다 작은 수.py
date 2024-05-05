class quest:
    def __init__(self):
        self.num_A,self.num_B = map(int,input().split())
        self.list_num = list(map(int,input().split()))
        self.print_list = []
    def check_small(self):
        for i in range(self.num_A):
            if self.list_num[i] < self.num_B:
                self.print_list.append(self.list_num[i])
        print(*self.print_list)

Quest =quest()
Quest.check_small()