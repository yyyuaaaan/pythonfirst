"""
Regular Expression Matching

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") false
isMatch("aa","aa") - true
isMatch("aaa","aa") - false
isMatch("aa", "a*") - true
isMatch("aa", ".*") - true
isMatch("ab", ".*") - true
isMatch("aab", "c*a*b") - true

not the same as wild card matching
The major difference is the meaning of  "*" in the string.

 bool isMatch_2(const char *s, const char *p) {
        if (*p == '\0') return *s == '\0';

        if (*s == *p || *p == '.' && *s != '\0')
            return *(p+1) != '*' ? isMatch(s+1, p+1) :
                                   isMatch(s+1, p) || isMatch(s, p+2);
        else
            return *(p+1) == '*' && isMatch(s, p+2);
    }
"""
def ismatch(s,p):
    if p is None: return s is None
    if s[0] == p[0] or p[0] is '.' and s[0] is not None:
        if p[1] is not '*':
            return ismatch(s[1:],p[1:])
        else:
            return ismatch(s[1:],p) or ismatch(s,p[2:])
    else:
        return p[1:] == '*' and ismatch(s,p[2:])