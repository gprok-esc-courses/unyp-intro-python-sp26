
class ParenthesesValidator:
    def __init__(self):
        self.word = ''
        self.stack = []
        self.states = [
            'START', 'LETTER', 'OPENING', 'CLOSING', 'END' 
        ]
        self.current = 'START'


    def validate(self, word):
        self.word = word
        for char in self.word:
            if char in '{[(':
                self.current = 'OPENING'
                self.opening(char)
            elif char in '}])':
                self.current = 'CLOSING'
                ok = self.closing(char)
                if not ok:
                    print("INVALID")
                    return
            else:
                self.current = 'LETTER'
        self.state = 'END'
        ok = self.end()
        if ok:
            print("VALID")
        else:
            print("INVALID")


    def opening(self, char):
        self.stack.append(char)

    def closing(self, char):
        if len(self.stack) == 0:
            return False
        else:
            last = self.stack.pop(-1)
            if (char == '}' and last == '{') or \
                (char == ']' and last == '[') or \
                (char == ')' and last == '('):
                return True 
            else:
                return False
            
    def end(self):
        if len(self.stack) > 0:
            return False
        else:
            return True


validatror = ParenthesesValidator()
s = input("Type string to validate: ")
validatror.validate(s)
