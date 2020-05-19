'''
2020-05-18
ARCFOUR aka RC4 stream cipher algorithm
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
    key = convert_string_to_codelist(key)
    text = convert_string_to_codelist(text)
    ks = keystream(key)
    output = []
    for c in text:
        output.append('{:02X}'.format(c ^ next(ks)))
    #TODO can this be compressed into a list comprehension?
    #TODO consider building output raw, then reformat to hex later?
    return ''.join(output) #converts list of bytes to string of bytes

def arcfour_decode(key, text):
    #TODO this
    pass

def convert_string_to_codelist(string):
    '''Convert a string to a list of codepoint values.'''
    '''Use to convert key from string to list for use in KSA.'''
    return [ord(c) for c in string]

def convert_codelist_to_hex_string(codelist):
    '''Convert a list of decimal codepoints to a string of hex'''
    return bytes(codelist).hex().upper()

def convert_hex_string_to_codelist(hexstring):
    return list(bytes.fromhex(hexstring))

def arctest():
    '''Test stuff.'''
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
