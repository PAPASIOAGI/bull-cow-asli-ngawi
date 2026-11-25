def hitung(rahasia, tebakan):
    BULL = 0
    COW = 0
    for i in range(4):
        if tebakan[i] == rahasia[i]:
            bull += 1
        elif tebakan[i] in rahasia[i]:
            cow += 1
    return (bull, cow)

def cek_tebakan(tebakan):
    if len(tebakan) != 4:
        return False
    if not tebakan.isdigit():
        return False
    if len(set(tebakan)) != 4:
        return False
    return True