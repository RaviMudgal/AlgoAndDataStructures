import re
# recursive function to check palindrome
def isPalindrome(text):
    text = re.sub('[^A-Za-z0-9]+', '', text) # regular expression to remove spaces
    # text = re.sub('\W+', '', text) works the same like re above
    if len(text) < 2:
        return True
    elif text[0] != text[-1]:
        return False
    return isPalindrome(text[1:-1])

print(isPalindrome('ayaaya'))
print(isPalindrome('ravi'))
print(isPalindrome('live not on evil'))
#print(isPalindrome('Reviled did I live, said I, as evil I did deliver'))# work to fix this case to remove punctuation
