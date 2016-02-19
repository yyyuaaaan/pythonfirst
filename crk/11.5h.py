"""__author__ = 'anyu'

11.5 Given a sorted array of strings which is interspersed with empty strings, write a method to
find the location of a given string.
Example: ["at","","","","ball","","","car","","","dad","",""] will return 4

Careful consideration should be given to the situation when someone searches for the empty string.
Should we find the location (which is an 0(n) operation)? Or should we handle this as an error?
There's no correct answer here. This is an issue you should raise with your interviewer.
Simply asking this question will demonstrate that you are a careful coder.
"""

def bsearch(a,start,end,s):

    # use another helper function to do array range check
    if not s:
        print("illegal input")
        return

    mid = (start+end)/2
    # if mid is "", just move right untill end.
    while a[mid]=="" and mid<end:
        mid+=1
    # if end still "", end bsearch the first half
    if mid==end:
        bsearch(a,start,(start+end)/2,s)
    if a[mid] == s: return mid


    elif s<a[mid]:
        bsearch(a,start,mid-1,s)
    else:
        bsearch(a,mid+1,end,s)

    return mid

a=["at","","","","ball","","","car","","","dad","",""]
print bsearch(a,0,12,"ball")
