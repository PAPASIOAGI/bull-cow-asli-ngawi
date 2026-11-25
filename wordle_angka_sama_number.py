import random

def hitung(rahasia, tebakan):
    BULL = 0
    COW = 0
    for i in range(4):
        if tebakan[i] == rahasia[i]:
            BULL += 1
        else:
            for j in range(4):
                if tebakan[i] == rahasia[j]:
                    COW += 1
    return (BULL, COW)

def cek_tebakan(tebakan):
    if len(tebakan) != 4:
        return ("ga valid mas, harus 4 digit cik")
    if not tebakan.isdigit():
        return ("harus angka mas, bukan huruf woilah")
    if len(set(tebakan)) != 4:
        return ("ga valid, jangan kayak password komdigi mas. mikirs kirk")
    return None

def buat_rahasia():

def main():

def uji():
    print(cek_tebakan("1234"))
    print(hitung("1807", "7810"))
print("Semua uji coba berhasil!")


uji()



