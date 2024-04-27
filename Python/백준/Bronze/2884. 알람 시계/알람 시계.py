
class Quest:
    def __init__(self):                                 # 설정한 알람 시간을 입력하는 함수 설정
        self.input = list(map(int,input().split()))
        self.time = [0,0]     
    def alarm_hour (self):
        if self.input[1] < 45:                          #설정한 알람 시간의 분이 45보다 작을 경우 1을 빼줌
            if self.input[0] == 0:                      #만약 입력한 알람 시간의 시가 0일 경우 결과값의 시는 23이 되게 설정
                self.time[0] = 23                       
            else:                                       # 아닐 경우 입력한 알람 시간의 시에서 1을 빼줌
                self.time[0] = self.input[0] - 1
        else:
            self.time[0] = self.input[0]
            pass
        return self.time[0]
    def alarm_minute(self):
        if self.input[1] >= 45:                      #설정한 알람 시간의 분이 45보다 클 경우, 입력한 알람 시간에서 45를 뺀 값이 결과 값의 분으로 출력
            self.time[1] = self.input[1] - 45
        else:                                       #설정한 알람 시간의 분이 45보다 작을 경우 입력한 알람 시간에서 15를 더한 값이 결과값의 분으로 출력
            self.time[1] = self.input[1] + 15      
        return self.time[1]

quest = Quest()
pass
print("{} {}".format(quest.alarm_hour(),quest.alarm_minute()))
pass