"""
An Amazon Fulfillment Associate has a set of items that 
need to be packed into two boxes. Given an integer array
of the item weights (arr) to be packed, divide the item
weights into two subsets, A and B, for packing into the
associated boxes, while respecting the following conditions:
- The intersection of A and B is null.
- The union A and B is equal to the original array.
- The number of elements in subset A is minimal.
- The sum of A's weights is greater than the sum of B's weights.
Return the subset A in increasing order.
If more than one subset meets the above conditions, return
the one with the maximal total sum of its elements.
Example:
arr = [3, 7, 5, 6, 2]
The two subsets that meet the conditions are [5, 7] and [6, 7].
The subset [6, 7] has the maximal total sum of 13, so the
answer is [6, 7].

Function Signature: def minimalHeaviestSetA(arr: List[int]) -> List[int]:
Input
- An integer array arr (2 <= len(arr) <= 10^5) where each element

"""
def minimalHeaviestSetA(arr):
    arr.sort()
    total_sum = sum(arr)
    half_sum = total_sum // 2
    subset_sum = 0
    
    for i in range((len(arr)-1), -1, -1):
        subset_sum += arr[i]
        if subset_sum > half_sum:
            return arr[i:]
    return []
minimalHeaviestSetA([3, 7, 5, 6, 2]) # [5, 7] and [6,7]