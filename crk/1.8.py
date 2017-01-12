"""

__author__ = 'anyu'

Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, si and s2, write code to check If s2 is a rotation
 of si using only one call to isSubstring (e.g., "waterbottLe" is a rotation of "erbottLewat").
"""

def strrotation(s1,s2):
    if len(s1) !=len(s2):
        return False
    stemp= s1+s1
    return isSubstring(s2,stemp)

def isSubstring2(sub1,sub2):
    """
    check if sub1 is in sub2
    """
    if len(sub1) > len(sub2):
        return False
    return sub2.find(sub1)  > -1


def isSubstring(sub1,sub2):
    """
    check if sub1 is in sub2
    """
    if len(sub1) > len(sub2):
        return False
    if not sub1: return True
    elif sub2.find(sub1[0]) is -1:
        return False
    else:
        i = sub2.find(sub1[0])
        return isSubstring(sub1[1:],sub2[i:])


print strrotation("waterbottle", "erbottLewat")
