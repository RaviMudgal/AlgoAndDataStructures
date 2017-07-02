import Stacks

def checkPar(symStr):
    s = Stacks.Stack()
    bal = True
    index = 0
    while index < len(symStr) and bal:
        sym = symStr[index]
        if sym == "(":
            s.push(sym)
        else:
            if s.isEmpty():
                bal = False
            else:
                s.pop()
        index += 1

    if bal and s.isEmpty():
        return True
    else:
        return False

print(checkPar("()()(())"))
print(checkPar("((())"))

