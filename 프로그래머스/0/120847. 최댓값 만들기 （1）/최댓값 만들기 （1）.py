def solution(numbers):
    numbers = sorted(numbers)
    x, y = numbers[-1], numbers[-2]
    return x*y