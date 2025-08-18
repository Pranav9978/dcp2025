import math

def merge(arr1, arr2, m, n):
    def next_gap(gap):
        if gap <= 1:
            return 0
        return math.ceil(gap / 2)

    gap = next_gap(m + n)
    while gap > 0:
        
        i = 0
        while i + gap < m:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        
        j = gap - m if gap > m else 0
        while i < m and j < n:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        
        j = 0
        while j + gap < n:
            if arr2[j] > arr2[j + gap]:
                arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
            j += 1

        gap = next_gap(gap)


arr1 = [1,2,5,]
arr2 = [3,4,7,8]
merge(arr1, arr2, len(arr1), len(arr2))
print("arr1:", arr1)
print("arr2:", arr2)