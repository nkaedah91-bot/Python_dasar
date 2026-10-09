def hitung_luas(panjang, lebar):
    """Menghitung luas persegi panjang."""
    luas = panjang * lebar
    return luas

hasil = hitung_luas(5, 3)
print(hasil)
print(hitung_luas(10, 2))
def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"

print(sapa("Nur Kaedah"))
print(sapa(salam="Hai", nama="Budi"))

def total(*angka):
    return sum(angka)

print(total(1, 2, 3, 4))
kuadrat = lambda x: x ** 2
print(kuadrat(4))  # 16

siswa = [("Nur Kaedah", 85), ("Budi", 95)]
print(max(siswa, key=lambda s: s[1]))
x = "global"

def tes():
    x = "lokal"  # hanya di dalam tes()
    print(x)     # lokal

tes()
print(x)         # global
