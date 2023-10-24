def encode(password):
    new = ""
    for i in password:
        a = int(i) - 3
        b = str(a)
        new += b
    return new

def decode(password):
    original = ""
    for i in password:
        a = int(i) - 3
        b = str(a)
        original += b
    return original


