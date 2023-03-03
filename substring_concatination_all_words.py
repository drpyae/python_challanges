def findSubstring(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []
    
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1
    
    word_len = len(words[0])
    window_len = len(words) * word_len
    result = []
    
    for i in range(len(s) - window_len + 1):
        window_words = {}
        for j in range(i, i+window_len, word_len):
            word = s[j:j+word_len]
            if word not in word_count:
                break
            if word not in window_words:
                window_words[word] = 0
            window_words[word] += 1
            if window_words[word] > word_count[word]:
                break
        else:
            result.append(i)
            
    return result
