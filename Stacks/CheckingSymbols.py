import Stacks

def checkSym(symStr):
    s = Stacks.Stack()
    bal = True
    index = 0
    while index < len(symStr) and bal:
        sym = symStr[index]
        if sym in "({[":
            s.push(sym)
        else:
            if s.isEmpty():
                bal = False
            else:
                top = s.pop()
                if not matchSym(top,sym):
                    bal = False
        index += 1
    if bal and s.isEmpty():
        return True
    else:
        return False

def matchSym(open,close):
    opens = "({["
    closers = ")}]"
    return opens.index(open) == closers.index(close)

print(checkSym("((({{[[)))}}]]"))
print(checkSym("(({{})(("))
print(checkSym("(){}[]"))
