class Capslock:
    string: str
    def __init__(self, string: str):
        self.string = string
    def uppercase(self):
        return self.string.upper()
    
s = Capslock('Meow')
print(s.uppercase())
