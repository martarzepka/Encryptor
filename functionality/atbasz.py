from functionality.alphabet import Alphabet


class Atbasz(Alphabet):
    def __init__(self):
        super().__init__()
        self._alphabet = []
        self._alphabetReverse = []

    def chooseAlphabet(self, alph):
        match alph:
            case 'en':
                self._alphabet = self.english
                self._alphabetReverse = self._alphabet.copy()
                self._alphabetReverse.reverse()
            case 'pl':
                self._alphabet = self.polish
                self._alphabetReverse = self._alphabet.copy()
                self._alphabetReverse.reverse()

    def encrypt(self, plainText, alph):
        cryptogram = ''
        self.chooseAlphabet(alph)

        for letter in plainText:
            if letter not in self._alphabet:
                cryptogram += letter
            else:
                index = self._alphabet.index(letter)
                cryptogram += self._alphabetReverse[index]

        return cryptogram

    def decrypt(self, cryptogram, alph):
        return self.encrypt(cryptogram, alph)
