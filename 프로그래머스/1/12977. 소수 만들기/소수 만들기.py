from itertools import combinations

def prime_list(limit):

    is_prime = [True] * (limit + 1)
    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    return [i for i in range(limit + 1) if is_prime[i]]

def solution(nums):
    max_sum = sum(sorted(nums)[-3:])
    primes = prime_list(max_sum)
    prime_set = set(primes)

    cnt = 0
    
    for combi in combinations(nums, 3):
        s = sum(combi)
        if s in prime_set:
            cnt += 1
            
    return cnt