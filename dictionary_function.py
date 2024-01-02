d1 = {"ankit":"kumar","arun":"maheshwri","rajat":"srivastav"}

print(d1)

d2 = d1.copy()
del d2["ankit"]
print(d1)


print(d1.get("ankit"))

d1.update({"sreha":"patwa"})
print(d1)

print(d1.keys())

print(d1.items())

