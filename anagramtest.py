from itertools import permutations

def isAnagram(s, t):
    if (len(t) > len(s)):
        print "len(t)>len(s) false"
        return False

    s = s.lower()
    t = t.lower()

    t = list(t)


    for i in xrange(1,len(t)+1):
        for subset in permutations(t, i):
            if len(subset) == len(t) and ''.join(subset) in s:
                print True
                return True

    print False
    return False

def main():
    isAnagram("eloHELLO", "hello")
    isAnagram("hi", "gefefef")
    isAnagram("wow wow", "wew")

if __name__ == "__main__":
    main()