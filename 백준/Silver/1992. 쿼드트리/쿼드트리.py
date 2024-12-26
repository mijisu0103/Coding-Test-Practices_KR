import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
video = []
for _ in range(N):
    v = [int(x) for x in list(input().rstrip())]
    video.append(v)

def quadtree(n, vlist):
    s = 0
    for l in vlist:
        s += sum(l)
    
    if s == n**2:
        return '1'
    if s == 0:
        return '0'
    
    half = n//2
    temp = '('
    temp += quadtree(half,[l[:half] for l in vlist[:half]])
    temp += quadtree(half,[l[half:] for l in vlist[:half]])
    temp += quadtree(half,[l[:half] for l in vlist[half:]])
    temp += quadtree(half,[l[half:] for l in vlist[half:]])
    temp += ')'
    
    return temp

print(quadtree(N, video))