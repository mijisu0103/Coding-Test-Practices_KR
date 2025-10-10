from collections import Counter

def solution(array):

    count = Counter(array)
    
    max_freq = max(count.values())
    
    max_freq_values = [key for key, value in count.items() if value == max_freq]
    
    if len(max_freq_values) > 1:
        return -1
    
    return max_freq_values[0]
