class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      """
      One approach to solving this problem is to use a hash set to keep track of the numbers that have already appeared in the array. 
      As we iterate through the array, we check if the current number is already in the hash set.
      If it is, we have found a duplicate and return True. If we iterate through the entire array without finding a duplicate, we return False.
      """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
