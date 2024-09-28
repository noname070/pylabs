

ROT = 13
from string import ascii_lowercase

def encrypt_caesar(plaintext: str) -> str:
    return "".join(chr((ord(c) - (ord("A") if c.isupper() else ord("a")) + ROT) % len(ascii_lowercase) + (ord("A") if c.isupper() else ord("a") )) if c.isalpha() else c for c in plaintext)

def decrypt_caesar(ciphertext: str) -> str: #        отличия вооот тут  \|/
    return "".join(chr((ord(c) - (ord("A") if c.isupper() else ord("a")) - ROT) % len(ascii_lowercase) + (ord("A") if c.isupper() else ord("a"))) if c.isalpha() else c for c in ciphertext)

if __name__ == "__main__":
    
    assert decrypt_caesar(encrypt_caesar("pY7h0|\| 15 $0 b0r1ng"))=="pY7h0|\| 15 $0 b0r1ng", RuntimeError("итс джавст не воркс")
    print('ok')