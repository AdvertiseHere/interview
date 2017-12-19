# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.


def question2(a):
    a_reversed = a[::-1]
    palindrome = ""

    for i in range(len(a)):
        match = ""
        for j in range(len(a_reversed)):
            if (i + j < len(a) and a[i + j] == a_reversed[j]):
                match += a_reversed[j]

            else:
                if (len(match) > len(palindrome)):
                    palindrome = match
                    match = ""

    return palindrome

def main():
    question2("helololhe")
    question2("jiwe234565432nnnw")


if __name__ == "__main__":
    main()