#https://quera.org/problemset/51865

Curent_point=int(input())
Days_on_travel= int(input())

if Days_on_travel==0:
    Curent_point=20
elif Days_on_travel==7:
    Curent_point=Curent_point
else:
    Curent_point =Curent_point-Days_on_travel

if Curent_point<0:
    Curent_point=0
print(Curent_point)
