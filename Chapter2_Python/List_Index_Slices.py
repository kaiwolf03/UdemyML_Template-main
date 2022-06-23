list_a = [i for i in range(10)]
print(list_a)

list_b = []
list_c = []
list_d = []
list_e = []


# ersten drei Werte aus list_a übernehmen
for i in range(3):
    list_b.append(list_a[i])

print(list_b)

# oder
list_c = [list_a[i] for i in range(3)]

print(list_c)

# oder slicing (best)
#         start:stop:step
list_d = list_a[0:3:1]
print(list_d)

list_e = list_a[0:3:2]
print(list_e)
