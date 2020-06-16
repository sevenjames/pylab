def meow(snack):
    (c, a, t, s) = (65, 26, 32, 13)
    purr = ''.join(chr(i) for i in range(c, c+a))
    chew = ''.join(chr(i) for i in range(c+t, c+a+t))
    eat = dict(zip(purr+chew, purr[s:]+purr[:s]+chew[s:]+chew[:s]))
    return ''.join([eat.get(bite, bite) for bite in snack])

def meowmeow(snack):
    (c, a, t) = (65, 26, 32)
    purr = ''.join(chr(i) for i in range(c, c+a))
    chew = ''.join(chr(i) for i in range(c+t, c+a+t))
    eat = ''.join(''.join(i) for i in list(zip(purr, chew)))
    return ''.join(eat[(eat.find(bite)+a)%(a+a)] if bite in eat else bite for bite in snack)

def give(s):
    return bytes.decode(bytes.fromhex(s))

def sample():
    tuna = '5572797962206a626579712e'
    print(meow(give(tuna)))

if __name__ == "__main__":
    sample()
