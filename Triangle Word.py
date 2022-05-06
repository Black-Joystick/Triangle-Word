

alphabets = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
total = 0
isTriangle = False
n = 1
word = input('Enter Word: ').lower()
if(word.isalpha()):
    for alph in word:
        total+=alphabets[alph]
    print('Word value of', word.upper(), 'is = ', total)

    while (n/2)*(n+1) <= total :
        if (n/2)*(n+1) == total:
            isTriangle = True
        n+=1
    if isTriangle :
        print('Well done,', word.upper(), 'is a triangle word.')
    else:
        print('Sorry,',word.upper(), 'is not a triangle word.')
else:
    print('Sorry can only deal with charachters A-z and a-z.')