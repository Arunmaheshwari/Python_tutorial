s = set()
#print(type(s))

# s2 = set({2, 4, 5})
# print(s2)

# s_from_list = set([1,2,3,4,5])
# print(s_from_list)
# print(type(s_from_list))


# l = [1,2,3,4,5]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))


# adding value in set

s.add(1)
# s.add("arun")
s.add(2)
s.add(3)
s.remove(3)
print(s)

#functions

# s1 = s.union({1,2,3})
# print(s, s1)
#
# s2  = s.intersection({1,2,3})
# print(s,s2)
#
# print(len(s))
# print(min(s))
# print(type(s))
# print(max(s))

s1 = {4,5}
print(s.isdisjoint(s1))



