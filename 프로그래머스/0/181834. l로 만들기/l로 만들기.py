def solution(myString):
    change = "abcdefghijk"
    translation = str.maketrans(change, 'l' * len(change))
    
    return myString.translate(translation)
