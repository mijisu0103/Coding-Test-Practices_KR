def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        if ("ayaaya" in b or "yeye" in b or "woowoo" in b or "mama" in b):
            continue

        for c in can:
            b = b.replace(c, " ")

        if b.strip() == "":
            answer += 1

    return answer