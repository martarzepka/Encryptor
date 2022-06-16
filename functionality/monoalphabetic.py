from functionality.alphabet import Alphabet


class Monoalphabetic(Alphabet):
    def __init__(self):
        super().__init__()
        self._alphabet = []
        self._alphabetWithKey = []

    def createAlphabet(self, key, alph):
        self._alphabetWithKey = []

        for letter in key:
            if letter not in self._alphabetWithKey:
                self._alphabetWithKey.append(letter)

        match alph:
            case 'en':
                self._alphabet = self.english
            case 'pl':
                self._alphabet = self.polish

        for letter in self._alphabet:
            if letter not in self._alphabetWithKey:
                self._alphabetWithKey.append(letter)

    def encrypt(self, plainText, key, alph):
        cryptogram = ''
        self.createAlphabet(key,alph)

        for letter in plainText:
            if letter not in self._alphabet:
                cryptogram += letter
            else:
                index = self._alphabet.index(letter)
                cryptogram += self._alphabetWithKey[index]

        return cryptogram

    def decrypt(self, cryptogram, key, alph):
        plainText = ''
        self.createAlphabet(key, alph)

        for letter in cryptogram:
            if letter not in self._alphabet:
                plainText += letter
            else:
                index = self._alphabetWithKey.index(letter)
                plainText += self._alphabet[index]

        return plainText
