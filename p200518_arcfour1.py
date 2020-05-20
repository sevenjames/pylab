'''
2020-05-18
ARCFOUR aka RC4 stream cipher algorithm
For educational purposes only.
'''

def KSA(key):
    '''Key Scheduling Algorithm'''
    keylen = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylen]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRNG(S):
    '''Pseudo-Random Number Generator Algorithm'''
    i, j = 0, 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K

def arcfour_crypt(key, text):
    '''Encrypt/decrypt a list of decimal integer bytes.'''
    keystream = PRNG(KSA(key))
    return [c ^ next(keystream) for c in text]


def convert_stringtxt_to_listbytes(stringtxt):
    ''' 'foo' >> [102, 111, 111] '''
    return [ord(c) for c in stringtxt]

def convert_listbytes_to_stringhex(listbytes):
    ''' [102, 111, 111] >> '666F6F' '''
    return bytes(listbytes).hex().upper()

def convert_stringhex_to_listbytes(stringhex):
    ''' '666F6F' >> [102, 111, 111] '''
    return list(bytes.fromhex(stringhex))

def convert_listbytes_to_stringtxt(listbytes):
    ''' [102, 111, 111] >> 'foo' '''
    return ''.join([chr(c) for c in listbytes])


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
        key = convert_stringtxt_to_listbytes(key)
        txt = convert_stringtxt_to_listbytes(txt)
        enc = arcfour_crypt(key, txt)
        enc = convert_listbytes_to_stringhex(enc)
        print('Actual:', enc)
        if enc == exp:
            print('Success')
        else:
            print('Error: output does not match expectation')
        print()


if __name__ == '__main__':
    arctest()
