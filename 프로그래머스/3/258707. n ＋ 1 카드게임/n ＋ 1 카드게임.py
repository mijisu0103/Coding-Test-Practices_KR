from collections import deque

def solution(coin, cards):
    
    n = len(cards)  # 전체 카드 수
    on_hands = set(cards[: n // 3]) # 손에 든 카드
    deck = deque(cards[n // 3 :]) # 덱에 남아 있는 카드 
    possible = set()  # 가능한 카드 조합을 저장할 집합

    def update_possible():
        """
        덱에 카드가 있으면 두 장을 뽑아서 possible (가능한 카드) 집합에 추가하는 함수
        """
        if deck:
            possible.add(deck.popleft())  # 덱에서 한 장 뽑아서 가능한 카드에 추가
            possible.add(deck.popleft())  # 덱에서 또 한 장 뽑아서 가능한 카드에 추가

    def remove_pair(source: set, target: set) -> bool:
        """
        주어진 source 집합에서 target 집합과 짝이 되는 카드를 찾아 제거하는 함수
        """
        nonlocal coin, round  # coin과 round를 외부에서 수정 가능하도록

        # source에서 하나씩 꺼내서 target에서 짝을 찾기
        for x in list(source):
            if (n + 1) - x in target:  # (n + 1) - x가 target에 있으면 짝을 찾은 것
                source.remove(x)  # source에서 x 제거
                target.remove((n + 1) - x)  # target에서 짝 제거
                return True  # 짝을 찾았으므로 True 반환
        return False  # 짝을 찾지 못했으므로 False 반환

    round = 1  # 게임 시작 시 첫 번째 라운드 설정
    
    # 덱에 카드가 남아 있는 동안 게임 진행
    while deck:
        update_possible()  # 덱에서 두 장의 카드를 뽑아서 가능한 카드 집합에 추가
        
        # 손에 든 카드에서 짝을 찾으면 라운드 진행
        if remove_pair(on_hands, on_hands):
            round += 1
        # 손에 든 카드에서 덱에서 나온 카드와 짝을 찾으면 코인을 1 소모하고 라운드 진행
        elif coin >= 1 and remove_pair(on_hands, possible):
            coin -= 1
            round += 1
        # 덱에서 나온 카드들끼리 짝을 찾으면 코인을 2 소모하고 라운드 진행
        elif coin >= 2 and remove_pair(possible, possible):
            coin -= 2
            round += 1
        else:
            break  # 짝을 찾지 못하면 게임 종료

    return round  # 총 라운드 수 반환