# reverse string using stack
import Stacks


def reverseString(text):
    stack = Stacks.Stack()
    for i in text:
        stack.push(i)
    revString = ""
    while not stack.isEmpty():
        revString += stack.pop()
    return revString


print(reverseString('asdddd'))
print(reverseString('My name is john'))
