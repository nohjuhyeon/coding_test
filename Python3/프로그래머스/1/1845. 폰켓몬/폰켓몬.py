def solution(nums):
    if int(len(nums)/2) > len(set(nums)):
        answer = len(set(nums))
    else:
        answer = int(len(nums)/2)
    return answer