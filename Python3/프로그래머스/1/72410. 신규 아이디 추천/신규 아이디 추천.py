import re 
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^a-z|0-9|\-|_|.]','',new_id)
    while True:
        after_id = new_id.replace('..','.')
        if after_id == new_id:
            break
        else:
            new_id = after_id
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    while True:
        if len(new_id) <= 2:
            new_id += new_id[-1]
        else:
            break
    answer = new_id
    return answer