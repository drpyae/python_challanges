def count_vowel_strings(words: List[str], left: int, right: int) -> int:
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    """
    To solve this problem, we can iterate over each word in the given range and count the number of vowel strings in each word. 
    We can use a helper function to check if a given string is a vowel string, by checking if its first and last characters are vowels.
    """
    
    def is_vowel_string(word: str) -> bool:
        if word[0] not in vowels:
            return False
        if word[-1] not in vowels:
            return False
        return True
    
    count = 0
    for i in range(left, right+1):
        if is_vowel_string(words[i]):
            count += 1
            
    return count
