"""

__author__ = 'anyu'
http://www.hawstein.com/posts/ctci-solutions-contents.html
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""

def is_unique_chars(input_string):
    """Using set as a hash table
    """

    if len(input_string)>256: # assume input string is ASCII
        return False
    return len(set(input_string))==len(input_string)


def is_unique_chars_3(input_string):
    """Using no data structure: complexity O(N^2)
    """
    if len(input_string) == 0:        # special use case: input is "", []
        print "input string length is zero"
        return
    if len(input_string)>256:
        return False

    for char in input_string:
        charindex = input_string.index(char)
        if char in input_string[charindex+1:]:
            return False
    return True

def hasuniquechar(s):
    """
    optimize:    len of s
    :param s:
    :return:
    """
    if not s:
        print "null input"
        return
    else:
        hashlist=set()
        #l=list(s) # [] is not gonna work
        for char in s:
            if char in hashlist:
                return False
            else:
                hashlist.add(char)
                print char
        return True
print hasuniquechar("~!@#$%^&*(")

print is_unique_chars_3("")
print is_unique_chars_3("sss")
print is_unique_chars_4("~!@#$%^&*(")

