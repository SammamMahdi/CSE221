def mergeSort(array, n):
    if n > 1:
        m = n // 2
        r = array[:m]
        l = array[m:]
        mergeSort(r, m)
        mergeSort(l,n-m)
        i = j = k = 0
        while i < m and j < n-m:
            if r[i] < l[j]:
                array[k] = r[i]
                i += 1
            else:
                array[k] = l[j]
                j += 1
            k += 1
        while i < m:
            array[k] = r[i]
            i += 1
            k += 1

        while j < n-m:
            array[k] = l[j]
            j += 1
            k += 1
