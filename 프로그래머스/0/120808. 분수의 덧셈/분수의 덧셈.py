import math

def solution(numer1, denom1, numer2, denom2):

    lcm = abs(denom1 * denom2) // math.gcd(denom1, denom2)
    
    num = numer1 * (lcm // denom1) + numer2 * (lcm // denom2)
    
    gcd = math.gcd(num, lcm)
    
    return [num // gcd, lcm // gcd]
