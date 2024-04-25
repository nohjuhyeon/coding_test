def solution(nums):
    answer = 0
    answer_list = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                answer_num = nums[i]
                answer_num += nums[j]
                answer_num += nums[k]
                answer_list.append(answer_num)
    repeat = int(max(answer_list)**0.5)+1
    check_list= []
    for i in range(2,repeat+1):
        for j in range(i*i,max(answer_list)+1,i):
            check_list.append(j)
    for i in range(len(answer_list)):
        if answer_list[i] not in check_list:
            answer += 1
    return answer