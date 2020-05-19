with open('words.txt', 'r') as file:
    words = file.readlines()
    for i in words:
        word = i.strip('\n')
        if list(word) == list(reversed(word)):
            print(word)