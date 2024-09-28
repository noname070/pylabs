from string import ascii_lowercase

def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    return "".join(
        chr((ord(c) - (ord("A") if c.isupper() else ord("a")) + (ord(keyword[i % len(keyword)].upper()) - ord("A"))) % len(ascii_lowercase) + (ord("A") if c.isupper() else ord("a"))) if c.isalpha() else c for i, c in enumerate(plaintext))

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    return "".join(
        chr((ord(c) - (ord("A") if c.isupper() else ord("a")) - (ord(keyword[i % len(keyword)].upper()) - ord("A"))) % len(ascii_lowercase) + (ord("A") if c.isupper() else ord("a"))) if c.isalpha() else c for i, c in enumerate(ciphertext))

if __name__ == "__main__":
    keyword = "BIBABOBAFLEXXX"
    assert decrypt_vigenere(encrypt_vigenere("pY7h0|\| 15 $0 b0r1ng", keyword=keyword), keyword=keyword)=="pY7h0|\| 15 $0 b0r1ng", RuntimeError("итс джавст не воркс")
    print('ok')