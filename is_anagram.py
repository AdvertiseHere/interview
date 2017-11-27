# def is_anagram(s, t):
#     s = str(s)
#     t = str(t)
#     sorted_t = t.sort()
#     print sorted_t
#     if sorted_t in s:
#         print True
#     else:
#         print False

def isAnagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    # convert str1 to a list
    str1_list = list(str1)

    # sort the list alphabetically
    sorted_str1 = sorted(str1_list)
    print sorted_str1

    # convert back to a string (now sorted alphabetically)
    str1_final = ''.join(sorted_str1)
    print str1_final

    # convert str2 to a list
    str2_list = list(str2)

    # sort the list alphabetically
    sorted_str2 = sorted(str2_list)

    # convert back to a string (now sorted alphabetically)
    str2_final = ''.join(sorted_str2)
    print str2_final

    if str2_final in str1_final:
        print "True"
    else:
        print "False"

isAnagram("hello", "eh")
isAnagram("123", "1234")
isAnagram("HELLO", "hoe")