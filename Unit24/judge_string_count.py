# 'the' 개수 출력 프로그램
import string
example = input().split()
count = 0
for i in example:
    word = i.strip(string.punctuation)
    if word == 'the':
        count += 1
print(count)