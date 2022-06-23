list_a = [100.0, 200.0, -10.0]
list_b = [False, False, True]

for i in range(len(list_a)):
    print(list_a[i], list_b[i])

print("")


# both values
for val_a, val_b in zip(list_a, list_b):
    print(val_a, val_b)

print("")

# index and one value
for i, val in enumerate(list_a):
    print(i, val)

print("")

# index and both values
for i, (val_a, val_b) in enumerate(zip(list_a, list_b)):
    print(i, val_a, val_b)
