def isPalindrome(letter):

    if len(letter)==1:
        return True

    else:
        return letter[0] ==letter[-1] and isPalindrome(letter[1:-1])


print(isPalindrome("dad"))