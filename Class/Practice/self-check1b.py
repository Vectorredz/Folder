from dataclasses import dataclass

@dataclass
class Capslock:
    string: str
    def uppercase(self) -> str | None:
       return self.string.upper()


s = Capslock('Meow')
print(s.uppercase())