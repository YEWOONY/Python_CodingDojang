def countdown(n):
    r = n + 1

    def count():
        nonlocal r
        r -= 1
        return r
    return count


n = int(input())

c = countdown(n)
for i in range(n):
    print(c(), end=' ')