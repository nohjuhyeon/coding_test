
import sys                                                                                      # sys 실행

class quest():
    def __init__(self):
        self.A = int(input())                                                                  # 입력한 반복횟수 self.A로 지정
        self.E = 0                                                                             # self.E는 0으로 지정
    def sum(self):
        for D in range(self.A):                                                                # self.A 만큼 반복
            B, C = map(int, sys.stdin.readline() .split())                                     # 더할 값 두 개 입력
            self.E = self.E + 1                                                                # 답안 번호 지정
            D = B + C 
            print("Case #{}: {} ".format(self.E,D))

Quest = quest()
Quest.sum()