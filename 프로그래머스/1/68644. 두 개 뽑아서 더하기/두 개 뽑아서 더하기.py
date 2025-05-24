from itertools import combinations
def solution(numbers):
    return sorted(set([i + j for i, j in combinations(numbers, 2)]))