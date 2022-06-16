from functionality.alphabet import Alphabet

class Caesar(Alphabet):
    def __init__(self):
        super().__init__()
        self._alphabet = []
        self._length = 0

    def chooseAlphabet(self, alph):
        match alph:
            case 'en':
                self._alphabet = self.english
                self._length = len(self.english)
            case 'pl':
                self._alphabet = self.polish
                self._length = len(self.polish)

    def encrypt(self, plainText, key, alph):
        cryptogram = ''
        self.chooseAlphabet(alph)

        for letter in plainText:
            if letter not in self._alphabet:
                cryptogram += letter
            else:
                index = self._alphabet.index(letter)
                index += int(key)
                index %= self._length
                cryptogram += self._alphabet[index]

        return cryptogram

    def decrypt(self, cryptogram, key, alph):
        plainText = ''
        self.chooseAlphabet(alph)
        for letter in cryptogram:
            if letter not in self._alphabet:
                plainText += letter
            else:
                index = self._alphabet.index(letter)
                index -= int(key)
                index += self._length
                index %= self._length
                plainText += self._alphabet[index]

        return plainText
