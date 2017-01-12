"""__author__ = 'anyu'
Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other.

  alist.sort()            ## correct
  alist = blist.sort()    ## NO incorrect, sort() returns None

   by using a hash table which maps from the sorted version of a word to a list of its anagrams
   So,forexample,acrewillmaptothelist{acre, race, care}. Once we've grouped all the words into these
   lists by anagram, we can then put them back into the array.
   but more space. though less time
"""

def sorta(arr):
    if not arr:
        return
    d=dict()
    for ele in arr:
        key = "".join(sorted(ele))
        d[key] = d.get(key,[])+[ele]
    for x in d.values():
        print x
    return

s =["axyz", "abc", "yzax", "bac", "zyxa", "fg", "gf"]
sorta(s)



def anagram(s1,s2):
    t1=list(s1).sort()#    sort() returns None, modifies the list   return sorted(s1) == sorted(s2)
    t2=list(s2).sort()
    return t1 == t2

def anagram2(s1,s2):
    return sorted(s1)==sorted(s2) #sorted("fsd") will return ['d', 'f', 's'], this is a new list
                                  #sort() can not be on string

def anagram_sort(lst):
    """
    sorted() built-in function that builds a new sorted list
    sort() returns None, modifies the list

    key specifies a function of one argument that is used to extract a comparison key from each
    list element: key=str.lower. The default value is None (compare the elements directly).
    """
    return sorted(lst, key=lambda elem: sorted(elem))



s =["axyz", "abc", "yzax", "bac", "zyxa", "fg", "gf"]

print anagram("abc","bac")
print anagram2("abc","bac")


print anagram_sort(s)





