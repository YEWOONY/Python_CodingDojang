text = input('문자열을 입력하세요: ')
for i in range(len(text)-1):
    print(i)
    print(text[i], text[i+1], sep='')