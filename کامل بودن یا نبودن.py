#https://quera.org/problemset/282

n = int(input())
zarf=[]
for i in range(1,n):
    if n%i==0:
        zarf.append(i)

if sum(zarf)==n:
    print("YES")
else:
    print("NO")
