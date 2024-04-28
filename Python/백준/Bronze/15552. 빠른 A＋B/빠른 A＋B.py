import sys                                                              # sys 불러오기
class quest():
    def __init__(self): 
        self.A = int(input())                                           # 입력한 반복횟수 self.A로 지정

    def sum(self):
        for D in range(self.A):                                         # self.A 만큼 반복
            B, C = map(int, sys.stdin.readline() .split())              # 더할 값 B,C 입력
            D = B + C                                                   # 덧셈
            print(D)                                

Quest = quest()
Quest.sum()