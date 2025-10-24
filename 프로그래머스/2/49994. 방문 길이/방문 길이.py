def solution(dirs):
    answer = 0
    x, y = 0, 0
    visited = set()

    for dir in dirs:

        if dir == 'U' and y < 5:
            next_x, next_y = x, y + 1
        elif dir == 'D' and y > -5:
            next_x, next_y = x, y - 1
        elif dir == 'R' and x < 5:
            next_x, next_y = x + 1, y
        elif dir == 'L' and x > -5:
            next_x, next_y = x - 1, y
        else:
            continue

        path = ((x, y), (next_x, next_y))
        reverse_path = ((next_x, next_y), (x, y))

        if path not in visited and reverse_path not in visited:
            visited.add(path)
            visited.add(reverse_path)
            answer += 1

        x, y = next_x, next_y

    return answer