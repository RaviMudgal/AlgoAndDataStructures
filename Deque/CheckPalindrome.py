import Deque


def checkPalindrome(word):
    s = Deque.Deque()
    for i in word:
        s.addRear(i)
    equal = True
    while s.size() > 1 and equal:
        first = s.removeFront()
        last = s.removeRear()
        if first != last:
            equal = False
    return equal


print(checkPalindrome('radar'))
print(checkPalindrome('ram mar'))
