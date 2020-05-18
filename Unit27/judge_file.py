with open('judge_words.txt', 'r') as file:
    words = file.read().split()
    for i in words:
        if 'c' in i: # 내가 한 방법 --> i.find('c') != -1
            print(i.strip(',.'))