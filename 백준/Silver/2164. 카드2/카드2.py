input  = int(input())
sq = 2

while(1):
    if (input == 1 or input == 2):
        print(input)
        break
    sq *= 2
    if(sq >= input):
        print((input - (sq // 2)) * 2)
        break