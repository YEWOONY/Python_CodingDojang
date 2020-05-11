a = [13, 52, 64, 36, 79]
smallest = a[0]
for i in a:
    if smallest > i:
        smallest = i
print(smallest)

biggest = a[0]
for i in a:
    if biggest < i:
        biggest = i
print(biggest)