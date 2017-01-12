def oneedit(s1, s2):
    """
    One Away: There are three types of edits that can be performed on strings:
    insert a character, remove a character, or replace a character.
    Given two strings, write a function to check if they are one edit (or zero edits) away.
    maybe recursion with suc is better.
    :param s1:
    :param s2:
    :return:
    """

    if s1==s2:
        return True
    elif len(s2)==len(s1):
        for i in range(len(s1)):
            if s2[i] != s1[i]:
                return s2[(i+1):] == s1[(i+1):]

    elif abs(len(s2)-len(s1))==1:
        if len(s1)-len(s2)==1:
            s1,s2=s2,s1
        for i in range(len(s1)):
            if s2[i] != s1[i]:
                return s2[(i+2):] == s1[(i+1):]
            elif i==len(s1)-1:
                return True
    else:
        return False

def oneedit2(s1, s2):
    if abs(len(s1)-len(s2))>1:
        return False
    elif len(s1)>len(s2):
        return oneedit2(s2,s1) # let s2 be longer
    else:
        i= 0
        shift = len(s2)-len(s1)
        xlen = len(s1)
        while i < xlen and s1[i] == s2[i]:
            i+=1

        if shift ==0:
            i+=1

        while i<xlen and s1[i]==s2[i+shift]:
            i+=1
        return i==xlen

print oneedit2("pale","ple")
print oneedit2("pales","pale")
print oneedit2("pale","bale")
print oneedit2("pale","bake")
