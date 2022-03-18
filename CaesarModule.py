import string

class CaesarCipher:
    def __init__(self, text, shift) -> None:
        self.text = text
        self.shift = shift

    def characters_all(self) -> list:
        return [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

    def reformatcharacters(self, chars, shift) -> list:
        return [x[shift:] + x[:shift] for x in chars]


    def caesar_encryption (self):
        characters_as_list = self.characters_all()
        characters_as_string = ''.join(self.reformatcharacters(characters_as_list, self.shift))
        character_trans = str.maketrans(''.join(characters_as_list), characters_as_string)
        return self.text.translate(character_trans)