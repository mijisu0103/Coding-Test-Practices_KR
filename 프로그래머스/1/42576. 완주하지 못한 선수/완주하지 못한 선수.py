def solution(participant, completion):
    hash_dict = dict()
    sumHash = 0
    
    for part in participant:
        hash_dict[hash(part)] = part
        sumHash += hash(part)
        
    for comp in completion:
        sumHash -= hash(comp)
        
    return hash_dict[sumHash]