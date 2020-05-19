text = 'this is python script'
words = text.split()            # 공백을 기준으로 문자열 분리하여 리스트 만듦

for i in range(len(words)-1):   # 2-gram, 리스트의 마지막에서 요소 한 개 앞까지만 반복
    print(words[i], words[i+1]) # 현재 문자열과 그 다음 문자열 출력