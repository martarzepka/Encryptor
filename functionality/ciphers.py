from functionality.alphabet import Alphabet
from functionality.atbasz import Atbasz
from functionality.caesar import Caesar
from functionality.monoalphabetic import Monoalphabetic

# the "Ciphers" class redirects the encryption and decryption to the appropriate ciphers
class Ciphers(Alphabet):
    def __init__(self):
        super().__init__()
        self._caesar = Caesar()
        self._atbasz = Atbasz()
        self._monoalphabetic = Monoalphabetic()
        self._alphabet = []

    def chooseAlphabet(self, alph):
        match alph:
            case 'en':
                self._alphabet = self.english
            case 'pl':
                self._alphabet = self.polish

    def prepareText(self, text, alph, removeOtherCh = False, removeSpaces = False):
        self.chooseAlphabet(alph)
        t = text
        t = t.upper()
        if alph == 'en':
            t = t.replace('Ą', 'A')
            t = t.replace('Ć', 'C')
            t = t.replace('Ę', 'E')
            t = t.replace('Ł', 'L')
            t = t.replace('Ń', 'N')
            t = t.replace('Ó', 'O')
            t = t.replace('Ś', 'S')
            t = t.replace('Ż', 'Z')
            t = t.replace('Ź', 'Z')

        if removeSpaces:
            t = t.replace(' ', '')
        t2 = ""
        if removeOtherCh:
            for letter in t:
                if letter in self._alphabet or letter == ' ':
                    t2 += letter
        else:
            t2 = t
        t2 = t2.strip()
        return t2

    def encrypt(self, plainText, cipher, alph, keyText = '', keyNumber = 3):
        match cipher:
            case 'caesar':
                return self._caesar.encrypt(plainText, keyNumber, alph)
            case 'atbasz':
                return self._atbasz.encrypt(plainText, alph)
            case 'monoalphabetic':
                key = self.prepareText(keyText, alph)
                return self._monoalphabetic.encrypt(plainText, key, alph)

    def decrypt(self, cryptogram, cipher, alph, keyText = '', keyNumber = 3):
        match cipher:
            case 'caesar':
                return self._caesar.decrypt(cryptogram, keyNumber, alph)
            case 'atbasz':
                return self._atbasz.decrypt(cryptogram, alph)
            case 'monoalphabetic':
                key = self.prepareText(keyText, alph)
                return self._monoalphabetic.decrypt(cryptogram, key, alph)
