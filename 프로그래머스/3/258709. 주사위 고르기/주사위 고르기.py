from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    
    
    answer = []
    dice_len = len(dice) # 주사위 개수
    max_cnt = 0 # 가장 많이 이길 수 있는 경우의 수

    # 주사위를 두 명에게 나누는 모든 경우의 수
    dice_dist_cases = combinations(range(dice_len), dice_len // 2)
    
    for case in dice_dist_cases:
        a_case = list(case) # a 주사위 인덱스
        b_case = [] # b 주사위 인덱스
        
        # b가 고른 주사위 = a가 고른 주사위 외의 나머지 주사위들
        for b in range(dice_len):
            if b not in a_case:
                b_case.append(b)
            
        # a가 선택한 주사위들의 가능한 점수 합 리스트
        a_case_list = [dice[temp] for temp in a_case]
        a_score_list = [sum(combination) for combination in product(*a_case_list)]
        
        # b가 선택한 주사위들의 가능한 점수 합 리스트
        b_case_list = [dice[temp] for temp in b_case]
        b_score_list = [sum(combination) for combination in product(*b_case_list)]
        
        cnt = 0 # a가 b를 이길 수 있는 경우의 수
        b_score_list.sort() # b 점수 리스트 오름차순 정렬
        
        for a in a_score_list:
            # b_score_list에서 a보다 작은 값들 개수 세기
            cnt += bisect_left(b_score_list, a)
        
        # 가장 많이 이기는 경우의 수 갱신
        if max_cnt < cnt:
            max_cnt = cnt
            answer = [a + 1 for a in a_case] # a가 고른 주사위들의 1-based 인덱스
        
    return answer