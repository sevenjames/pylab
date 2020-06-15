def meow(snack):
    (c, a, t) = (65, 26, 32)
    (m, e, o, w) = (c, c+a, c+t, c+a+t)
    purr = ''.join(chr(i) for i in range(m, e))
    hiss = ''.join(chr(i) for i in range(o, w))
    chew = ''.join(''.join(i) for i in list(zip(purr, hiss)))
    return ''.join(chew[(chew.find(bite)+a)%(a+a)] if bite in chew else bite for bite in snack)

def give(s):
    return bytes.decode(bytes.fromhex(s))

tuna = '5572797962206a626579712e'

print(meow(give(tuna)))
