def hitung(rahasia, tebakan):
    BULL = 0
    COW = 0
    for i in range(4):
        if tebakan[i] == rahasia[i]:
            BULL += 1
        elif tebakan[i] in rahasia[i]:
            COW += 1
    return (BULL, COW)

def cek_tebakan(tebakan):
    if len(tebakan) != 4:
        return False
    if not tebakan.isdigit():
        return False
    if len(set(tebakan)) != 4:
        return False
    return True

def uji():
    print(cek_tebakan("1234"))
    print(hitung("1234", "1234"))
print("Semua uji coba berhasil!")


uji()