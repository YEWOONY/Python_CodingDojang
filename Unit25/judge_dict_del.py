keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))
x = dict({key: value for key, value in x.items() if key != 'delta' and value != 30})

print(x)
