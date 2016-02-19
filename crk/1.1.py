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

def is_unique_chars_2(input_string):
    """Using list as a vector, similar when we do counting sort
    """
    if len(input_string) == 0:        # special use case: input is "", []
        print "input string length is zero"
        return
    if len(input_string)>256:       # >256,must not be unique.
        return False

    char_vector=[False]*256   # False*256 wrong!

    for char in input_string:
        if char_vector[ord(char)] == True:
            return False
        else:
            char_vector[ord(char)] = True
    return True


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

def is_unique_chars_4(input_string):
    """
    Using a char_list, O(N^2)
    """
    char_list = []
    for char in input_string:
        if char in char_list:
            return False
        else:
            char_list.append(char)
    return True

print is_unique_chars_3("")
print is_unique_chars_3("sss")
print is_unique_chars_4("~!@#$%^&*(")

