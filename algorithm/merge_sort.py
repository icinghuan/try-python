def merge_sort(a, l, r):
    if l >= r:
        return a
    mid = (l + r + 1) >> 1
    a = merge_sort(a, l, mid - 1)
    a = merge_sort(a, mid, r)
    i = l
    j = mid
    t = []
    while i < mid and j <= r:
        if a[i] > a[j]:
            t.append(a[j])
            j = j + 1
        else:
            t.append(a[i])
            i = i + 1
    while i < mid:
        t.append(a[i])
        i = i + 1
    while j <= r:
        t.append(a[j])
        j = j + 1
    a[l:r + 1] = t
    return a


if __name__ == '__main__':
    a = [10, 2, 5, 7, 1, 6, 4, 3, 9, 8, 11, 15, 20, 18, 12, 14, 13, 19, 17]
    print(merge_sort(a, 0, len(a) - 1))
