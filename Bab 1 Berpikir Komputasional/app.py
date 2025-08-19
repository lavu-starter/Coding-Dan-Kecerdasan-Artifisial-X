# Input nilai siswa
nilai = [80, 70, 90, 60, 85]

# Hitung rata-rata
rata_rata = sum(nilai) / len(nilai)

# Tentukan lulus atau tidak
if rata_rata >= 75:
    print("Lulus dengan rata-rata:", rata_rata)
else:
    print("Tidak Lulus dengan rata-rata:", rata_rata)
