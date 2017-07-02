import Stacks


def convertToBin(number):
    binStack = Stacks.Stack()
    while number > 0:
        remainder = number % 2
        binStack.push(remainder)
        number = number // 2

    binStr = ""
    while not binStack.isEmpty():
        binStr += str(binStack.pop())
    return binStr

print(convertToBin(1233))
print(convertToBin(10))

