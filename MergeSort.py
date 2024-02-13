def mergeSort(array):
    if len(array) > 1:
        #  r is the point where the array is divided into two subarrays
        m = len(array) // 2
        r = array[:m]
        l = array[m:]

        # Sort the two halves
        mergeSort(r)
        mergeSort(l)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(r) and j < len(l):
            if r[i] < l[j]:
                array[k] = r[i]
                i += 1
            else:
                array[k] = l[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(r):
            array[k] = r[i]
            i += 1
            k += 1

        while j < len(l):
            array[k] = l[j]
            j += 1
            k += 1
