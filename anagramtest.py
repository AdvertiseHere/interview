# Question 1
# Given two strings s and t, determine whether some anagram of t
# is a substring of s. For example: if s = "udacity" and t = "ad",
# then the function returns True. Your function definition should
# look like: question1(s, t) and return a boolean True or False.



from itertools import permutations

def isAnagram(s, t):

    # We confirm that s is longer than t.
    # If not, we know it cannot be a substring.
    if (len(t) > len(s)):
        print "len(t)>len(s) false"
        return False

    # Convert to lowercase so this function is not case-sensitive.
    s = s.lower()
    t = t.lower()

    t = list(t)


    for i in xrange(1,len(t)+1):
        for j in permutations(t):
            if ''.join(j) in s:
                print True
                return True

    print False
    return False

def main():
    isAnagram("eloHELLO", "lelo")
    isAnagram("hi", "gefefef")
    isAnagram("wow wow", "wew")
    isAnagram("12345", "21")

if __name__ == "__main__":
    main()