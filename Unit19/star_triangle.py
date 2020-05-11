#내 코드
# for i in range(5):
#     for j in range(0, i+1):
#         print('*', end='')
#     print()

#코딩도장 코드
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()