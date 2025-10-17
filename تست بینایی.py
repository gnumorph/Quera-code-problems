#https://quera.org/problemset/2659

Num=int(input())  #number of letters in input
Board=input()     #the word in front of student
Student=input()   # the word student says
wrongs=[]
for i in range(Num):
    if Board[i]==Student[i]:
        continue
    else:
        wrongs.append(i)

print(len(wrongs))