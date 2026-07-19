def selectionsort(l):
    n = len(l)

    if n < 1:
        return l

    for i in range(n):
        mpos = i

        for j in range(i + 1, n):
            if l[j] < l[mpos]:
                mpos = j

        l[i], l[mpos] = l[mpos], l[i]

    return l

l = [12,5,34,76,23,35,98]
print(selectionsort(l))