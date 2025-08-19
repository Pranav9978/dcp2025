def find_leaders(arr):
    n = len(arr)
    leaders = []
    for i in range(n):
        is_leader = True
        for j in range(i + 1, n):
            if arr[i] <= arr[j]:
                is_leader = False
                break
        if is_leader:
            leaders.append(arr[i])
    return leaders


arr = [16, 17, 4, 3, 5, 2]
print("Leaders :", find_leaders(arr))