a = [i * j for j in range(2, 10)
           for i in range(1, 10)]

b = [i * j for i in range(1, 10)
           for j in range(2, 10)]

print(a)
print(b)