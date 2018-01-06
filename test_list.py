foo = [4, 5, 6, 7, 8]
list_len = len(foo)

for idx in range(list_len):
    print(idx)
    print(foo[idx])


foo[2], foo[3] = foo[3], foo[2]

print(foo)
