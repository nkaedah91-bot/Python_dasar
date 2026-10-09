nilai = 80

if nilai >= 75:
    print("Selamat, kamu lulus!")
else:
    print("Ayo remedial dulu")

print("Program selesai")
nilai = 78

if nilai >= 85:
    grade = "A"
elif nilai >= 70:
    grade = "B"
elif nilai >= 55:
    grade = "C"
else:
    grade = "D"

nama = "Nur Kaedah"
umur = 21
print(f"Nama: {nama}, Umur: {umur} tahun")
print(f"Nilai {nilai} → grade {grade}")
hari = "sabtu"

match hari:
    case "sabtu" | "minggu":
        print("Libur!")
    case "senin":
        print("Semangat!")
    case _:
        print("Hari kerja")