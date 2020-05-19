word = input()
for i in range(int(len(word) / 2)):
    if word[i] != word[-(i+1)]:
        flag = False
    else:
        flag = True
if flag:
    print(word + ' is palindrome')
else:
    print(word + ' is not palindrome')
