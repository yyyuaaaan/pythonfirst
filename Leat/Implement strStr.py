"""
// Implement strStr().
//
// Returns a pointer to the first occurrence of needle in haystack,
// or null if needle is not part of haystack.
//
// Complexity:
// brute force, O(n*m) time, O(1) space
// Knuth-Morris-Pratt Algorithm (KMP), O(n+m) time, O(n) space


The strstr function locates a specified substring within a source string.
Strstr returns a pointer to the first occurrence of the substring in the source.
If the substring is not found, strstr returns a null pointer.

 Assume that N = length of string, M = length of substring, then the complexity is O(N*M).
 Try writing the code down on a piece of paper. Remember to test for special cases.

 char *strStr1(char *haystack, char *needle) {
        if (haystack == NULL || needle == NULL) return NULL;
        int n = strlen(haystack), m = strlen(needle);
        for (int i = 0; i <= n - m; i++) {
            int j = 0;
            while (j < m && haystack[i + j] == needle[j]) j++;
            if (j == m) return haystack + i;
        }
        return NULL;

"""
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    # just substringneedle in string haystack problem, why bother renaming!

def strStr(haystack, needle):
    if not haystack or not needle: return None
    n = len(haystack)
    m = len(needle)
    for i in range(n-m+1):
        j = 0
        while j < m and haystack[i+j]==needle[j]:
            j+=1
        if j == m:
            return i
        return None
