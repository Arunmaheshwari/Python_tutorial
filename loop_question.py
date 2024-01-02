# print that no from list which is greater then 55 and has numaric value

items = ["arun", "tarun",34,5,76,98,32,1,3,876,55]

for item in items:
    if str(item).isnumeric() and item>55:
        print(item)