"""
Notes:
 Given a string s and a dictionary of words dict, determine if s can be segmented into
 a space-separated sequence of one or more dictionary words.
 For example, given
 s = "leetcode",
 dict = ["leet", "code"].
 Return true because "leetcode" can be segmented as "leet code".

 Solution: dp.

"""

def wordBreak(s, dict):
    if not s: return False
    if s in dict: return True
    for i in range(len(s)):
        if (s[:i] in dict):
            return wordBreak(s[i:],dict)
    return False
print wordBreak("leetcode",["leet", "code"])

print wordBreak("ab", ["a","b"])