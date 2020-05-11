h = int(input())
for i in range(h):
    for j in range(h-1, -1, -1):
        if j <= i:
            print('*', end='')
        else:
            print(' ', end='')
    for j in range(h):
        if j < i:
            print('*', end='')
    print()