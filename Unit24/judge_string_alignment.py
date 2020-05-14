# 높은 가격순
prices = sorted(list(map(int, input().split(';'))), reverse=True)
for i in prices:
    print('{0:>9,}'.format(i))
