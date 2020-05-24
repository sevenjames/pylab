"""
2020-05-18
ARCFOUR aka RC4 stream cipher algorithm.
References:
https://tools.ietf.org/html/draft-kaukonen-cipher-arcfour-03
https://en.wikipedia.org/wiki/RC4
For educational purposes only.

BUG : Only works on single-byte text characters.
Conversion functions assume single-byte text.
Multi-byte characters raise error: ValueError: bytes must be in range(0, 256)

TODO: process file at byte level. content encoding is irrelevant.
arcfour inputfile outputfile
    if args count is not 2, fail, print usage
    if inputfile doesn't exist, fail, print error
    if outputfile does exist, fail, print error
    load inputfile
    process file
    write outputfile
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
    return [b ^ next(keystream) for b in dat]

def encrypt(key, dat):
    """Encrypt text string to string of hex bytes."""
    key = convert_textstring_to_bytelist(key)
    dat = convert_textstring_to_bytelist(dat)
    return convert_bytelist_to_hexstring(cipher(key, dat))

def decrypt(key, dat):
    """Decrypt string of hex bytes to string."""
    key = convert_textstring_to_bytelist(key)
    dat = convert_hexstring_to_bytelist(dat)
    return convert_bytelist_to_textstring(cipher(key, dat))

def convert_textstring_to_bytelist(textstring):
    """ 'foo' >> [102, 111, 111] """
    return [ord(c) for c in textstring]

def convert_bytelist_to_hexstring(bytelist):
    """ [102, 111, 111] >> '666F6F' """
    return bytes(bytelist).hex().upper()

def convert_hexstring_to_bytelist(hexstring):
    """ '666F6F' >> [102, 111, 111] """
    return list(bytes.fromhex(hexstring))

def convert_bytelist_to_textstring(bytelist):
    """ [102, 111, 111] >> 'foo' """
    return ''.join([chr(b) for b in bytelist])

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

def nonascii_test():
    """Test text with non-ascii character."""
    print(encrypt('foo','băr'))

if __name__ == '__main__':
    # vector_tests()
    nonascii_test()
