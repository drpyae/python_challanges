def trim_and_find_index(nums, queries):
    ans, trimmed = [], {}
    for k, trimi in queries:
        if trimi not in trimmed:
            trimmed[trimi] = sorted([(num[-trimi:], i) for i, num in enumerate(nums)])
        ans.append(trimmed[trimi][k-1][1])
    return ans
"""
  In this code, we first initialize an empty dictionary trimmed to store the trimmed numbers.
For each query, we check if the key trimi is already in trimmed.
If not, we create a new entry in trimmed with key trimi and value as a sorted list of tuples containing the trimmed number and its index in nums.
We then append the index of the k-th smallest trimmed number in nums to the ans list. 
We access the corresponding value in the trimmed dictionary using trimmed[trimi] and then retrieve the k-th smallest number using trimmed[trimi][k-1]. 
Finally, we append the index of the number (trimmed[trimi][k-1][1]) to the ans list.
Note that this code assumes that the input nums is a list of strings, not a list of integers. 
If nums is a list of integers, we would need to convert each integer to a string before applying string slicing.
"""
