def solution(price):
    
    if price >= 500_000:
        price *= 0.8
    elif price >= 300_000:
        price *= 0.9
    elif price >= 100_000:
        price *= 0.95

    return int(price)