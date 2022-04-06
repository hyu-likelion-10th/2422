import re

def solution(new_id):
    new_id = new_id.lower()
    
    for character in '~!@#$%^&*()=+[{]}:?,<>/':
        new_id = new_id.replace(character, '')
        
    new_id = re.sub('\.(\.)+', '.', new_id)
    
    while len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]
    while len(new_id) != 0 and new_id[len(new_id)-1] == '.':
        new_id = new_id[:-1]

    if new_id == '':
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        while len(new_id) != 0 and new_id[len(new_id)-1] == '.':
            new_id = new_id[:-1]

    while len(new_id) < 3:
        new_id = new_id + new_id[len(new_id) - 1]
        
    answer = new_id
    return answer