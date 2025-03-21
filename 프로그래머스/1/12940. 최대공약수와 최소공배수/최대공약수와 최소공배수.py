def solution(n, m):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    g = gcd(n, m)
    lcm = n * m // g
    
    return [g, lcm]
