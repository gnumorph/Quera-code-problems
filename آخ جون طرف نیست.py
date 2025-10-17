#https://quera.org/problemset/3538


num1=input()       # number of present days
p1_pday=input().split()   #first persons present days
num2=input()      # number of present days
p2_pday=input().split()      #second persons present days
num3=input()      # number of present days
p3_pday=input().split()      #3ed persons present days
Days_can_go=[]
# i did not gave a damn about the numbers 
alldays= p1_pday+p2_pday+p3_pday
weekdays=["shanbe","1shanbe","2shanbe","3shanbe","4shanbe","5shanbe","jome"]
for day in weekdays:
    if day not in set(alldays):
        Days_can_go.append(day)

print(len(Days_can_go))
