def meow(s):
    u = ''.join([chr(i) for i in range(65,91)])
    l = ''.join([chr(i) for i in range(97,123)])
    a = ''.join([''.join(i) for i in list(zip(u,l))])
    return ''.join([a[(a.find(c)+26)%52] if c in a else c for c in s])

def give(s):
    return bytes.decode(bytes.fromhex(s))

def pack(s):
    return bytes.hex(str.encode(s))

tuna = '5572797962206a626579712e'
print(meow(give(tuna)))
