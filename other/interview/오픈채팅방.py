def solution(record):
    '''
    tmp[0] = Action
    tmp[1] = Uid
    tmp[2] = UserName
    '''
    answer = []
    user = {}
    for item in record:
        tmp = item.split(" ")
        action = tmp[0]
        uid = tmp[1]
        if action == 'Enter' or action == 'Change':
            userName = tmp[2]
            user[uid] = userName    
            
    for item in record:
        tmp = item.split(" ")
        action = tmp[0]
        uid = tmp[1]
        userName = user[uid]
        if action == "Enter":
            text = userName + "님이 들어왔습니다."
            answer.append(text)
        elif action == "Leave":
            text = userName + "님이 나갔습니다."
            answer.append(text)
    return answer