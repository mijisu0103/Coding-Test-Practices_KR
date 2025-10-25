def solution(n, arr1, arr2):
    answer = []
    
    for n1, n2 in list(zip(arr1,arr2)):
        
        bin_str = bin(n1 | n2)[2:].zfill(n)
        bin_str = bin_str.replace('1','#')
        bin_str = bin_str.replace('0',' ')
        answer.append(bin_str) 
    
    return answer