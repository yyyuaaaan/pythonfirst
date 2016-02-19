"""

__author__ = 'anyu'

Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end of
the string to hold the additional characters, and that you are given
the "true" length of the string. (Note: if implementing in Java, please use a
character array so that you can perform this operation inplace.)

"""
def replace_str(str):
    """
    convert str to a list
    also, in this case we can use list as a backup queue
    good thing about python list, it is assumed unlimited length
    """
    lstr = []
    for char in str:
        if char ==" ":
            lstr.append("%20")
        else:
            lstr.append(char)

    return "".join(lstr)


print replace_str("fsda s sfda fds")


