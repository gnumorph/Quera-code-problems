#https://quera.org/problemset/280

numbers = sorted([int(input()) for _ in range(3)])
a,b,c = numbers

#conditin for fisaghoores
if (a**2)+(b**2)==(c**2):
    print("YES")
else:
    print("NO")
