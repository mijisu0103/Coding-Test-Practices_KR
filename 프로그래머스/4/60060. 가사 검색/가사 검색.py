from bisect import bisect_left, bisect_right
from collections import defaultdict

def count_value(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index - left_index

def solution(words, queries):
    answer = []
    array = defaultdict(list)
    reversed_array = defaultdict(list)

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for key in array.keys():
        array[key].sort()
        reversed_array[key].sort()

    for query in queries:
        if query[0] == '?':
            count = count_value(reversed_array[len(query)], query[::-1].replace('?', 'a'),
                                query[::-1].replace('?', 'z'))
        else:
            count = count_value(array[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))

        answer.append(count)
    return answer