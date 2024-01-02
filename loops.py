# list1 = [1,2,3,4,5,6,7]
# for item in list1:
#     print(item)


# list2 = [["arun",1],["varun",4], ["tarun",2],["jatin",7]]
# for i in list2:
#     print(i)

list2 = [["arun",1],["varun",4], ["tarun",2],["jatin",7]]
# for i, no in list2:
#     print(i, no)

dict1 = dict(list2)
print(dict1)

# for i in dict1:
#     print(i)

# it will give us error
# for i, j in dict1:
#     print(i,j)

# we can remove that error by this

for i, j in dict1.items():
    print(i,j)