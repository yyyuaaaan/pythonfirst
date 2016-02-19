"""

__author__ = 'anyu'

Implement a method to perform basic string compression using the counts of repeated characters
aabcccccaa would become a2blc5a3.
do nothing if this would not make the string smaller.
"""

def str_compress(strinput):
    """
    very tricky question, border conditions, be careful
    0(N) time and 0(N) space.
    """

    str_comp=[]
    count = 1
    for i in range(len(strinput)-1):
        if strinput[i] != strinput[i+1] :  # because have to consider the i+1 element, may array overflow
            str_comp.append(strinput[i]+str(count))
            count = 1
        else:
            count += 1

    str_comp.append(strinput[-1]+str(count)) # an-1 = an; an-1 != an; two condition same

    if len(str_comp) >= len(strinput):
        return ''.join(strinput)
    else:
        return ''.join(str_comp)


def str_compress2(strinput):
    """ another way: simple, use index as pointer! use 2 pointer p1 p2, use while
    use count anyway, pointer is complex
    """
    if len(strinput) <= 1: return strinput

    tempoutput = []
    starter = 0
    rider = 1
    while 0 <= starter <=len(strinput)-2: #starter in range(0,len(strinput)-1) wrong , range is a iterator

        while  1 <= rider <= len(strinput)-1:
            if strinput[starter] == strinput[rider]:
                rider+=1
        tempoutput.append(strinput[starter]+rider-starter)

        starter = rider
        rider +=1
        print "dd"
        break





print str_compress2("abc")
print str_compress2("aabc")
print str_compress2("aabcccccabbdssssd")
