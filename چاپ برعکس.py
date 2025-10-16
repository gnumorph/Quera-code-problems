#https://quera.org/problemset/3405

array=[]
x=""
while x!="0":
    x=input()
    array.append(x)

del(array[-1])

for  i in reversed(array):
    print(i)
