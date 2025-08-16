def find_num(arr):
    n = len(arr) + 1  
    expectedsum = n * (n + 1) // 2
    actualsum = sum(arr)
    return expectedsum - actualsum

arr = [1, 2, 4, 5]
print("Missing number:", find_num(arr))