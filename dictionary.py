da = {}
print(type(da))

d2 = {"Arun":"Maheshwari","Tarun":"Jain","Varun":"kumar","arpit":"bhargav"}

print(d2)
print(d2["Arun"])

d3 = {"Arun":"Maheshwari","Tarun":"Jain","Varun":"kumar","arpit": {"bhargav","kumar","varun"}}
print(d3["arpit"])

d4 = {"Arun":"Maheshwari","Tarun":"Jain","Varun":"kumar","arpit": {"arpita":"bhargav","arvita":"kumar","tarvita":"varun"}}
print(d4["arpit"])
print(d4["arpit"]["arpita"])


d4["ankit"] = "sharma"
print(d4)

del d4["ankit"]
print(d4)
