import numpy  

def solution(board, moves):
    answer = 0
    stack = []
    t_matrix = numpy.transpose(board) 
    for row in t_matrix: 
        print(row)
    
    for item in moves:
        for i in range(len(t_matrix[item - 1])):
            if t_matrix[item - 1][i] != 0:
                if len(stack) != 0:
                    if stack[-1] == t_matrix[item - 1][i]:
                        answer += 2
                        t_matrix[item - 1][i] = 0
                        stack.pop()
                    else:
                        stack.append(t_matrix[item - 1][i])
                        t_matrix[item - 1][i] = 0
                else:
                    stack.append(t_matrix[item - 1][i])
                    t_matrix[item - 1][i] = 0
                
                break
                
    return answer


def solution(s):
    answer = []
    tmp = s.split("{")
    numbers = []
    # 숫자를 parse 합니다
    for item in list(tmp):
        num = ""
        arr = []
        for elem in item:
            if elem != "" and elem != "}" and elem != ",":
                num += elem
            if elem == ",":
                arr.append(num)
                num = ""
            if elem == "}":
                arr.append(num)
                numbers.append(arr)
                break;
    sorted_arr = sorted(numbers, key=len)
    stack = []
    for i in range(len(sorted_arr)):
        for item in sorted_arr[i]:
            if item not in stack:
                answer.append(int(item))
                stack.append(item)
                break
            
    return answer

import itertools

def solution(user_id, banned_id):
    answer = 0
    # Store available combination
    dic = {}
    
    # For each banned_id
    for i in range(len(banned_id)):
        # For each user
        for j in range(len(user_id)):
            # If same length
            if len(banned_id[i]) == len(user_id[j]):
                for k in range(len(user_id[j])):
                    if banned_id[i][k] == user_id[j][k] or banned_id[i][k] == "*":
                        pass
                    else:
                        break
                    # If it matches
                    if k == len(banned_id[i]) - 1:
                        if i not in dic:
                            dic[i] = [user_id[j]]
                        else:
                            dic[i].append(user_id[j])
        
    all_comb = sorted(dic)
    combinations = itertools.product(*(dic[Name] for Name in all_comb))
    final = set(combinations)
    real_final = []
    for item in final:
        if len(set(item)) == len(banned_id):
            real_final.append(list(set(item)))
            
            
    tmp = []
    
    for item in real_final:
        if sorted(item) not in tmp:
            answer += 1
            tmp.append(sorted(item))
        

    return answer


def solution(k, room_number):
    answer = []
    rooms = list(range(1, k+1))
    
    for room in room_number:
        if room not in answer:
            answer.append(room)
            rooms.remove(room)
        else:
            a_rooms = list(filter(lambda x: x > room, rooms))
            answer.append(min(a_rooms))
            rooms.remove(min(a_rooms))
            
    return answer

def solution(stones, k):         
    answer = 0
    flag = False
    while flag is False:
        tmp = 0
        for i in range(len(stones)):
            if tmp == k:
                flag = True
                break;
            if stones[i] != 0:
                stones[i] -= 1
                tmp = 0
            elif stones[i] == 0:
                tmp += 1
        if tmp == k:
            break
        answer += 1
    return answer