#https://quera.org/problemset/3539

n = int(input().strip())

while n >= 10:
    s = 0
    x = n
    while x > 0:
        s += x % 10
        x //= 10
    n = s

print(n)
