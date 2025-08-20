def zero_sum_subarrays(arr):
    prefix = 0
    seen_map = {0: [-1]}
    result = []

    for idx, val in enumerate(arr):
        prefix += val

        if prefix in seen_map:
            for start in seen_map[prefix]:
                result.append((start + 1, idx))

        seen_map.setdefault(prefix, []).append(idx)

    return result


arr = [1, 2, -3, 3, -1, 2]
print(zero_sum_subarrays(arr))