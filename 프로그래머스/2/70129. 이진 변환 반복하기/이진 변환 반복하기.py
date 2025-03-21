def solution(s):
    answer = []
    cnt = 0     
    zeroCnt = 0
    
    while True:
        if s == "1":
            break;
            
        zeroCnt += s.count("0")  #문자열의 0의 개수 세기
        s = s.replace("0",'')    #0을 공백으로 변환
        s = bin(len(s))[2:]      #2진수로 변환
        
        cnt +=1
        
    answer = [cnt, zeroCnt]    
    return answer