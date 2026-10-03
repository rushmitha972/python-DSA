# Single occurrence
def linearsearch(a, el):
    for i in range(len(a)):
        if a[i] == el:
            return i
    return -1

a = [12, 3, 14, 22, 56, 75, 14]
print(linearsearch(a, 14))


# Multiple occurrence
def linearsearch(a, el):
    ar = []
    for i in range(len(a)):
        if a[i] == el:
            ar.append(i)

    if len(ar) > 0:
        return ar
    return -1

a = [12, 3, 14, 22, 56, 75, 14]
print(linearsearch(a, 14))