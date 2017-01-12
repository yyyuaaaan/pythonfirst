"""

__author__ = 'anyu'

Implement a method to perform basic string compression using the counts of repeated characters
aabcccccaa would become a2blc5a3.
do nothing if this would not make the string smaller.
"""

def str_compress(s):
    '''
    aabbbccccdsfa this is right
    :param s:
    :return:
    '''
    if not s:
        print "null input"
        return s
    else:
        i =0
        count=1
        temp=[]
        while i<=len(s)-1:
            if i == len(s)-1:
                temp.append(s[i])
                temp.append(str(count))
            elif s[i] != s[i+1]:
                temp.append(s[i])
                temp.append(str(count))
                count =1

            else:
                count+=1
            i+=1

        if len(temp)<len(s):
            return ''.join(temp)
        else:
            return s

def str_compress2(strinput):
    """ another way: simple, use index as pointer! use 2 pointer p1 p2, use while
    use count anyway, pointer is complex
    two inline while loop can be complex, so generally only use one while loop to make it much simpler
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
print str_compress("aabcccccabbdssssd")
