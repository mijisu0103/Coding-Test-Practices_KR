def solution(num_list):
    
    even_sum = 0
    odd_sum = 0
    
    for e in range(0, len(num_list), 2):
        even_sum += num_list[e]
    for o in range(1, len(num_list), 2):
        odd_sum += num_list[o]
        
    
    return max(even_sum, odd_sum)