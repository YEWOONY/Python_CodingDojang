# 지뢰찾기 내 버전
# 완전 노가다
col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        count = 0
        if matrix[i][j] == '*':
        # 지뢰일 때
            print('*', end='')
        elif matrix[i][j] == '.':
        # 지뢰가 아닐 때
            if i == 0:
                if j == 0:
                    if matrix[i][j+1] == '*':
                        count += 1
                    if matrix[i+1][j] == '*':
                        count += 1
                    if matrix[i+1][j+1] == '*':
                        count += 1
                elif j < col - 1:
                    if matrix[i][j-1] == '*':
                        count += 1
                    if matrix[i][j+1] == '*':
                        count += 1
                    if matrix[i+1][j-1] == '*':
                        count += 1
                    if matrix[i+1][j] == '*':
                        count += 1
                    if matrix[i+1][j+1] == '*':
                        count += 1
                elif j == col - 1:
                    if matrix[i][j-1] == '*':
                        count += 1
                    if matrix[i+1][j-1] == '*':
                        count += 1
                    if matrix[i+1][j] == '*':
                        count += 1
            elif i < row - 1:
                if j == 0:
                    if matrix[i-1][j] == '*':
                        count += 1
                    if matrix[i-1][j+1] == '*':
                        count += 1
                    if matrix[i][j+1] == '*':
                        count += 1
                    if matrix[i+1][j] == '*':
                        count += 1
                    if matrix[i+1][j+1] == '*':
                        count += 1
                elif j < col - 1:
                    if matrix[i-1][j-1] == '*':
                        count += 1
                    if matrix[i-1][j] == '*':
                        count += 1
                    if matrix[i-1][j+1] == '*':
                        count += 1
                    if matrix[i][j-1] == '*':
                        count += 1
                    if matrix[i][j+1] == '*':
                        count += 1
                    if matrix[i+1][j-1] == '*':
                        count += 1
                    if matrix[i+1][j] == '*':
                        count += 1
                    if matrix[i+1][j+1] == '*':
                        count += 1
                elif j == col - 1:
                    if matrix[i-1][j-1] == '*':
                        count += 1
                    if matrix[i-1][j] == '*':
                        count += 1
                    if matrix[i][j-1] == '*':
                        count += 1
                    if matrix[i+1][j-1] == '*':
                        count += 1
                    if matrix[i+1][j] == '*':
                        count += 1
            elif i == row - 1:
                if j == 0:
                    if matrix[i-1][j] == '*':
                        count += 1
                    if matrix[i-1][j+1] == '*':
                        count += 1
                    if matrix[i][j+1] == '*':
                        count += 1
                elif j < col - 1:
                    if matrix[i-1][j-1] == '*':
                        count += 1
                    if matrix[i-1][j] == '*':
                        count += 1
                    if matrix[i-1][j+1] == '*':
                        count += 1
                    if matrix[i][j-1] == '*':
                        count += 1
                    if matrix[i][j+1] == '*':
                        count += 1
                elif j == col - 1:
                    if matrix[i-1][j-1] == '*':
                        count += 1
                    if matrix[i-1][j] == '*':
                        count += 1
                    if matrix[i][j-1] == '*':
                        count += 1
            print(count, end='')
    print()