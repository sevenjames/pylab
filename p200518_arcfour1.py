'''
2020-05-18
ARCFOUR aka RC4 stream cipher algorithm.
References:
https://tools.ietf.org/html/draft-kaukonen-cipher-arcfour-03
https://en.wikipedia.org/wiki/RC4
For educational purposes only.
'''

def ksa(key):
    '''Key Scheduling Algorithm'''
    keylen = len(key)
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % keylen]) % 256
        s[i], s[j] = s[j], s[i]
    return s

def prng(s):
    '''Pseudo-Random Number Generator Algorithm'''
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        yield k

def cipher(key, bytelist):
    '''Process a list of decimal integer bytes with ARCFOUR stream cipher.'''
    keystream = prng(ksa(key))
    return [b ^ next(keystream) for b in bytelist]


def convert_textstring_to_bytelist(textstring):
    ''' 'foo' >> [102, 111, 111] '''
    return [ord(c) for c in textstring]

def convert_bytelist_to_hexstring(bytelist):
    ''' [102, 111, 111] >> '666F6F' '''
    return bytes(bytelist).hex().upper()

def convert_hexstring_to_bytelist(hexstring):
    ''' '666F6F' >> [102, 111, 111] '''
    return list(bytes.fromhex(hexstring))

def convert_bytelist_to_textstring(bytelist):
    ''' [102, 111, 111] >> 'foo' '''
    return ''.join([chr(b) for b in bytelist])

# TODO write main interface function to take inputs

# TODO write functions for decrypt and encrypt

def encrypt(key, txt):
    pass

def arctest():
    '''Vector Tests'''
    test_vectors = [
        ('Key', 'Plaintext', 'BBF316E8D940AF0AD3'),
        ('Wiki', 'pedia', '1021BF0420'),
        ('Secret', 'Attack at dawn', '45A01F645FC35B383552544B9BF5')]
    for vector in test_vectors:
        key, txt, exp = vector
        print('Key:', key)
        print('Text:', txt)
        print('Expect:', exp)
        key = convert_textstring_to_bytelist(key)
        txt = convert_textstring_to_bytelist(txt)
        enc = cipher(key, txt)
        enc = convert_bytelist_to_hexstring(enc)
        print('Actual:', enc)
        if enc == exp:
            print('Success')
        else:
            print('Error: output does not match expectation')
        print()


if __name__ == '__main__':
    arctest()
