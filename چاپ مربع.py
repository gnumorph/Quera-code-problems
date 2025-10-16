#https://quera.org/problemset/591

n = int(input())

# سطر اول
print('*' * n)

# سطرهای میانی
for i in range(n - 2):
    print('*' + ' ' * (n - 2) + '*')

# سطر آخر
print('*' * n)
