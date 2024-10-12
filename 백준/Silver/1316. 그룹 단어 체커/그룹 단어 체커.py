n = int(input())
group_word = n

for i in range(n):
    word = input()
    
    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            continue
        elif word[j] in word[j+1:]:
            group_word -= 1
            break
        
print(group_word)