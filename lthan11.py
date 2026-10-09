import csv

data = []

with open("nilai.csv") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

print(len(data), "baris")
print(data[0])
import csv

data = []
with open("nilai.csv") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])
        data.append(baris)

nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)

print(f"Rata-rata: {rata:.1f}")

lulus = [
    d["nama"] for d in data
    if d["nilai"] >= 75
]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])
rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")
