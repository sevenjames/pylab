"""
ARCFOUR aka RC4 stream cipher algorithm in Python 3.
2020-05-18
References:
https://tools.ietf.org/html/draft-kaukonen-cipher-arcfour-03
https://en.wikipedia.org/wiki/RC4
For educational purposes only.
TODO: new program: process file at byte level. content encoding is irrelevant.
"""

def ksa(key):
    """Key Scheduling Algorithm that builds the Substitution Box s."""
    keylen = len(key)
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % keylen]) % 256
        s[i], s[j] = s[j], s[i]
    return s

def prng(s):
    """Pseudo-Random Number Generator produces random byte k."""
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        yield k

def cipher(key, dat):
    """XOR bytes of dat with bytes from PRNG and return the result."""
    keystream = prng(ksa(key))
    return bytes(b ^ next(keystream) for b in dat)

def encrypt(key, dat):
    """Encrypt text string to string of hex bytes."""
    key = string_to_bytes(key)
    dat = string_to_bytes(dat)
    return bytes_to_hex(cipher(key, dat))

def decrypt(key, dat):
    """Decrypt string of hex bytes to string."""
    key = string_to_bytes(key)
    dat = hex_to_bytes(dat)
    return bytes_to_string(cipher(key, dat))

def string_to_bytes(s):
    """ 'băr' >> b'b\xc4\x83r' """
    return str.encode(s)

def bytes_to_hex(b):
    """ b'b\xc4\x83r' >> '62C48372' """
    return b.hex().upper()

def hex_to_bytes(h):
    """ '62C48372' >> b'b\xc4\x83r' """
    return bytes.fromhex(h)

def bytes_to_string(b):
    """ b'b\xc4\x83r' >> 'băr' """
    return bytes.decode(b)

def vector_tests():
    """Vector tests using known plaintexts and ciphertexts."""
    test_vectors = [
        ('Key', 'Plaintext', 'BBF316E8D940AF0AD3'),
        ('Wiki', 'pedia', '1021BF0420'),
        ('Secret', 'Attack at dawn', '45A01F645FC35B383552544B9BF5')]
    print('TEST ENCRYPTION ALGORITHM')
    for vector in test_vectors:
        key, txt, exp = vector
        out = encrypt(key, txt)
        print('Key:', key)
        print('Text:', txt)
        print('Expect:', exp)
        print('Actual:', out)
        print('Success' if out == exp else 'Fail', '\n')
    print('TEST DECRYPTION ALGORITHM')
    for vector in test_vectors:
        key, txt, exp = vector
        out = decrypt(key, exp)
        print('Key:', key)
        print('Data:', exp)
        print('Expect:', txt)
        print('Actual:', out)
        print('Success' if out == txt else 'Fail', '\n')
    print('TEST MULTI-BYTE CHARACTERS')
    print('foo, băr, C9E66E5B', encrypt('foo', 'băr'))
    print('foo, C9E66E5B, băr', decrypt('foo', 'C9E66E5B'))

if __name__ == '__main__':
    vector_tests()
