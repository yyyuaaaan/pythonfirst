"""
// Given a string, determine if it is a palindrome, considering only
// alphanumeric characters and ignoring cases.
//
// For example,
//
// "A man, a plan, a canal: Panama" is a palindrome.
// "race a car" is not a palindrome.
//
// Complexity:
// O(n) time, O(1) space
Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
    bool isPalindrome2(string & s) {
        int start = 0, end = s.size() - 1;
        while (start < end) {
            while (start < end && !isalnum(s[start])) start++;
            while (start < end && !isalnum(s[end])) end--;
            if (tolower(s[start]) != tolower(s[end])) return false;
            start++, end--;
        }
        return true;
    }
class Solution {
public:
    bool isPalindrome(string s) {
        for (int i = 0, j = s.size() - 1; i < j; ++i, --j)
        {
            while (i < j && !isalnum(s[i])) i++;
            while (i < j && !isalnum(s[j])) j--;

            if (tolower(s[i]) != tolower(s[j]))
                return false;
        }
        return true;
    }
};

    bool isPalindrome(const string &s) {
        int i = 0, j = s.size()-1;
        while (i < j) {
            if (s[i] != s[j]) return false;
            i++; j--;
        }
        return true;

"""
def ispalindrome(s):
    if s is "": return True
    start = 0
    end = len(s)-1

    def ischar(c):
        if ord(c)>=ord('a') and ord(c)<=ord('z')   or ord(c)>= ord('A') and ord(c)<=ord('Z'): return True
        else: return False


    while start<end:
        while start < end and (ischar(s[start]) is False): start+=1
        while start < end and (ischar(s[end]) is False): end -=1
        if s[start].lower() != s[end].lower(): return False # forget lower() to lower, hard to debug
        start +=1
        end -=1
    return True

print ispalindrome("A man, a plan, a canal: Panama")

