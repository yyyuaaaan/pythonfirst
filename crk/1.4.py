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



def replacestr(s):
    spacecount=0
    lenofs=len(s)
    for char in s:
        if char ==' ':
            spacecount+=1

    temp=[None]*(lenofs+2*spacecount)
    indexofstr=lenofs-1
    indexoflist=len(temp)-1
    while indexofstr >= 0:
        if s[indexofstr] == ' ':
            temp[indexoflist]='0'
            indexoflist-=1
            temp[indexoflist]='2'
            indexoflist-=1
            temp[indexoflist]='%'
            indexoflist-=1
            indexofstr-=1
        else:
            temp[indexoflist]=s[indexofstr]
            indexoflist -= 1
            indexofstr -=1


