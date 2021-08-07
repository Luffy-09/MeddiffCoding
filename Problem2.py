
def isPalindrome(word):
    rev = word[::-1]
    return word.upper() == rev.upper()

print(isPalindrome('Malayalam'))
print(isPalindrome('Himanshu'))