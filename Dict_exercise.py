dic = {
    "arun":"Maheshwari",
    "varun":"kumar",
    "jatin":"sharma",
    "rohit":"singh",
    "sristhi":"pare"
}

print("Enter name")

name = input()
print(dic.get(name))


# another way

#print(dic.get(input()))


# i will try this when i am able to use loops
"""if(name==dic.keys):
    print(dic.get(name))"""