def hitung(rahasia, tebakan):
    BULL = 0
    COW = 0
    for i in range(4):
        if tebakan[i] == rahasia[i]:
            bull += 1
        elif tebakan[i] in rahasia[i]:
            cow += 1
    return (bull, cow)


