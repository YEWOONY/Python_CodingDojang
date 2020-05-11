# 지뢰찾기 코딩도장 정답
# 이렇게 짧아지다니..
col, row = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

for r in range(row):
    for c in range(col):
        if matrix[r][c] == '*':
            print(matrix[r][c], end='')
            continue
        elif matrix[r][c] == '.':
            matrix[r][c] = 0
            for y in range(r - 1, r + 2):
                for x in range(c - 1, c + 2):
                    if y < 0 or y >= row or x < 0 or x >= col:
                        continue
                    if matrix[y][x] == '*':
                        matrix[r][c] += 1
        print(matrix[r][c], end='')
    print()