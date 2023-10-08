'''
==================== Challenge 03 ========================
Silahkan membuat: 
Tipe Data 
Variabel 
Konstanta
Pemberian Nilai 
Menampilkan Nilai dan 
Ekspressi (expression) dengan menggunakan Phyton.
Dokumen yang dituliskan terdiri dari:
Penjelasan
Code 
Hasil Output (print sreen) 
Outputnya wajib menampilkan nama dan nim Anda saat dijalankan (compile).
================= Challenge 03 ===========================
'''

# Meminta input dari pengguna melalui keyboard
nama = input("Masukkan Nama Anda: ")
nim = input("Masukkan NIM Anda: ")
mata_kuliah = "Pengenalan Pemrograman"
nilai_ujian = float(input("Masukkan Nilai Ujian Anda: "))

# Konstanta
PASSING_GRADE = 70

# Menampilkan Informasi Mahasiswa
print("\n==========Sistem Informasi Mahasiswa===========")
print('')
print("Selamat datang, " + nama + " NIM: " + nim + "")
print("Mata Kuliah: " + mata_kuliah)

# Menampilkan Nilai Ujian
print("Nilai Ujian: " + str(nilai_ujian))

# Memeriksa Apakah Lulus atau Tidak
if nilai_ujian >= PASSING_GRADE:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

print("Status: " + status)

# Menentukan Predikat Kelulusan
if nilai_ujian >= 93:
    predikat = "A (Sangat Baik)"
elif nilai_ujian >= 84:
    predikat = "B (Baik)"
else:
    predikat = "C (Kurang)"

print("Predikat Kelulusan: " + predikat)

# String untuk Pesan Kelulusan
pesan_kelulusan = f"Selamat, Anda telah {status.lower()} dalam ujian {mata_kuliah.lower()} dengan nilai {nilai_ujian:.2f}!"
print(pesan_kelulusan)

print('');
print("==========Sistem Informasi Mahasiswa=============")
