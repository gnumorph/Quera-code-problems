#https://quera.org/problemset/10230

nums = list(map(int,input().split()))
if sum(nums)==180 and all(angle > 0 for angle in nums):
    print("Yes")
else:
    print("No")
