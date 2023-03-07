class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k
"""
To solve this problem, we can use a binary search algorithm to find the k-th missing positive integer.
We can start by initializing two pointers, left and right, to the first and last elements of arr respectively. 
We then use binary search to find the smallest index mid such that the number of missing positive integers before arr[mid] is greater than or equal to k.
To count the number of missing positive integers before arr[mid],
we can use the fact that the difference between consecutive elements of arr should be equal to 1.
If the difference between arr[mid] and the element before it is less than k, then the k-th missing positive integer must be after arr[mid]. Otherwise,
the k-th missing positive integer must be before arr[mid]. We can continue the binary search until we find the smallest mid that satisfies the condition.

In this code, we first initialize left and right to the first and last indices of arr respectively. We then use a while loop to perform binary search.

In each iteration, we compute the middle index mid as the average of left and right.

We then check if the number of missing positive integers before arr[mid] is less than k by computing arr[mid] - mid - 1.

If this value is less than k, then the k-th missing positive integer must be after arr[mid], so we update left to mid + 1. 

Otherwise, the k-th missing positive integer must be before arr[mid], so we update right to mid - 1.

We repeat this process until we find the smallest index mid such that the number of missing positive integers before arr[mid] is greater than or equal to k. 

We then return the k-th missing positive integer, which is arr[mid] - (mid + 1 - k).

Note that we add k to left in the return statement to get the index of the k-th missing positive integer. 

We subtract (mid + 1 - k) from arr[mid] to get the value of the k-th missing positive integer.
"""
