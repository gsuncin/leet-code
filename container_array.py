# [7, 1, 2, 3, 9] -> 7, 9 H x W -> 7X4 -> 28 area
# [6, 9, 3, 4, 5, 8]


# def findMaxContainerArea(height: list[int]):
#     results = [0] * len(height)
#     if len(height) <= 1:
#         return 0
#     for x in range(len(height)):
#         for y in range(len(height)):
#             results[x] = max(results[x], (min(height[x], height[y]) * (y - x)))
#     return max(results)


def findMaxContainerArea(height: list[int]):
    l, r = 0, len(height) - 1
    result = 0
    while l < r:
        result = max(result, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return result


print(findMaxContainerArea([7, 1, 2, 3, 9]))  # 28
print(findMaxContainerArea([6, 9, 3, 4, 5, 8]))  # 32
print(findMaxContainerArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
