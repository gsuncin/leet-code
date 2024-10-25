# Given an array of integers, return the indices of two numbers that add up to a given target


# [1, 3, 7, 9, 2] -> 11 = 9, 2 => [3, 4]
# def findSumIndices(arr, target):
#     for x in range(len(arr)):
#         for y in range(len(arr)):
#             if arr[x] == arr[y]:
#                 continue
#             if arr[x] + arr[y] == target:
# return [x, y]


def findSumIndices(arr, target):
    arr_set = set()  # {}
    for el in range(len(arr)):
        if target - arr[el] in arr_set:  # 2
            return [arr.index(target - arr[el]), el]
        arr_set.add(arr[el])  # 4


print(findSumIndices([3, 2, 4], 6))
# print(findSumIndices([1, 3, 7, 9, 2], 11))
