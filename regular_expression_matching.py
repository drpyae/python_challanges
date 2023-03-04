class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Regular expression matching with support for '.' and '*' can be implemented using dynamic programming.
        We can define dp[i][j] as a boolean value indicating whether the substring s[:i] matches the pattern p[:j].
        The base case is dp[0][0] = True, which means an empty string matches an empty pattern.
        Then, we can consider three cases:
        If p[j-1] is a non-wildcard character, then s[i-1] and p[j-1] must match, and dp[i][j] is dp[i-1][j-1].
        If p[j-1] is a wildcard character '.' that matches any single character, then dp[i][j] is dp[i-1][j-1].
        If p[j-1] is a wildcard character '*' that matches zero or more of the preceding element, then there are two possibilities:
        a. The '*' matches zero characters, so dp[i][j] is dp[i][j-2].
        b. The '*' matches one or more characters, so s[i-1] and the preceding character in p must match, and dp[i][j] is dp[i-1][j].
        """
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
    
        for i in range(m+1):
            for j in range(1, n+1):
                if p[j-1] != '*':
                    dp[i][j] = i > 0 and (s[i-1] == p[j-1] or p[j-1] == '.') and dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-2] or (i > 0 and (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
        
        return dp[m][n]
