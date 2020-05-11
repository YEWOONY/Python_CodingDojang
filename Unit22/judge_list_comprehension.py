n1, n2 = map(int, input().split())
a = [2 ** i for i in range(n1, n2+1)]
# del a[1]
# del a[-2]
a.pop(1)
a.pop(-2)
print(a)