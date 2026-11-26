import random

rahasia_subject = "6712"

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
    rahasia = ""
    while len(set(rahasia)) < 4:
        rahasia = str(random.randint(0, 9999)).zfill(4)
    return rahasia


def main():
    rahasia = buat_rahasia()
    print("Selamat datang di wordle ada angka sama number")
    print("Tebak angka 4 digit dengan digit yang berbeda.")
    while True:
        tebakan = input("Masukkan jawaban: ")

        validasi = cek_tebakan(tebakan)
        if validasi is not None:
            print(validasi)
            continue

        bulls, cows = hitung(rahasia, tebakan)

        print(f"BULLS: {bulls}, COWS: {cows}")
        if bulls == 4:
            print("Selamat! Anda berhasil menebak angka rahasia!")
            break


def uji():
    assert cek_tebakan("1234") is None, "harusnya valid"
    assert cek_tebakan("123") == "ga valid mas, harus 4 digit cik"
    assert cek_tebakan("12ab") == "harus angka mas, bukan huruf woilah"
    assert (
        cek_tebakan("1123")
        == "ga valid, jangan kayak password komdigi mas. mikirs kirk"
    )
    assert hitung("1234", "1234") == (4, 0)
    assert hitung("1234", "4321") == (0, 4)
    assert len(buat_rahasia()) == 4 and len(set(buat_rahasia())) == 4
    print("Semua pengujian berhasil!")


main()



