class Solution:
	
"""
We maintain two pointers: read and write. The read pointer scans through the input array,
and for each group of consecutive repeating characters, we compute its length, and write the compressed output to the write pointer. 
The anchor pointer points to the start of the current group of repeating characters.

We iterate until read reaches the end of the array. At each iteration, 
we check whether read is at the end of the array, or whether the character at read is different from the next character. 
If so, we write the current character (from anchor) to chars[write], and increment write.

If the current group of characters has length greater than 1, we need to append the length of the group to the output.
Since we're only allowed to use constant extra space, we can't use a separate buffer to store the count. Instead, 
we convert the count to a string, and write each digit of the count to chars[write].

Finally, we update anchor to point to the start of the next group of characters.

The time complexity of this algorithm is O(n), where n is the length of the input array. 
The space complexity is O(1), since we only use constant extra space.
"""
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write, anchor = 0, 0
        for read in range(n):
            if read == n - 1 or chars[read] != chars[read + 1]:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    count = str(read - anchor + 1)
                    for c in count:
                        chars[write] = c
                        write += 1
                anchor = read + 1
        return write
