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

def keystream(key):
    '''Create the keystream generator object.'''
    '''Key must be a list of decimal values. Conversion is handled elsewhere.'''
    S = KSA(key)
    return PRNG(S)

def arcfour_encode(key, text):
    # TODO only accept lists as input. preconvert them elsewhere.
    key = convert_stringtxt_to_listbytes(key)
    text = convert_stringtxt_to_listbytes(text)
    ks = keystream(key)
    #build list of hex bytes
    output = ['{:02X}'.format(c ^ next(ks)) for c in text]
    # convert list of hex bytes to string of hex bytes
    return ''.join(output)
    #TODO consider building output raw, then reformat to hex later?

def arcfour_decode(key, text):
    #TODO write decode function
    pass

def convert_stringtxt_to_listbytes(stringtxt):
    '''Convert a string of text to a list of bytes.
    'foo' >> [102, 111, 111] '''
    return [ord(c) for c in stringtxt]

def convert_listbytes_to_stringhex(codelist):
    '''Convert a list of bytes to a string of hex bytes.
    [102, 111, 111] >> '666F6F' '''
    return bytes(codelist).hex().upper()

def convert_stringhex_to_listbytes(hexstring):
    '''Convert string of hex bytes to a list of bytes.
    '666F6F' >> [102, 111, 111] '''
    return list(bytes.fromhex(hexstring))

def convert_listbytes_to_stringtxt():
    '''Convert list of bytes to string of text. (use chr()?)
    [102, 111, 111] >> 'foo' '''
    pass

def arctest():
    tv_keys = ['Key',
               'Wiki',
               'Secret']
    tv_txts = ['Plaintext',
               'pedia',
               'Attack at dawn']
    tv_cyph = ['BBF316E8D940AF0AD3',
               '1021BF0420',
               '45A01F645FC35B383552544B9BF5']
    for i in range(len(tv_keys)): # PEP8 C0200
        #TODO use: for i,item in enumerate(sequence):
        enc = arcfour_encode(tv_keys[i], tv_txts[i])
        print('Key:', tv_keys[i])
        print('Text:', tv_txts[i])
        print('Expect:', tv_cyph[i])
        print('Actual:', enc)
        if enc == tv_cyph[i]:
            print('Success!')
        else:
            print('Poop!')
        print()

arctest()