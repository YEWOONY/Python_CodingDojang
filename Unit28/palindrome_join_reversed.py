word = input('단어를 입력하세요: ')
# join은 구분자 문자열과 문자열 리스트의 요소를 연결함
# 빈 문자열에 reversed(word)의 요소를 연결하면 뒤집힌 문자열을 얻을 수 있음
print(word == ''.join(reversed(word)))
