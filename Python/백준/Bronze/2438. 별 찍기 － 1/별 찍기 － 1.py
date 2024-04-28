class quest:
    def __init__(self):
        self.num_input = int(input())                                          # 반복 횟수 입력
    def star(self):
        for i in range(self.num_input):                                       # 반복 횟수만큼 반복 출력
            for j in range(i+1):                                              # 줄이 추가 될때마다 별의 개수 증가
                print("*",end="")
            print("")

Quest = quest()
Quest.star()