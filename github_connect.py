# Data mahasiswa
mahasiswa = [
    {"NPM": 1, "Nama": "MAFTUH", "Angkatan": 2024, "Alamat": "PALEMBANG"},
    {"NPM": 2, "Nama": "NICO ROBIN", "Angkatan": 2004, "Alamat": "MESUJI"},
    {"NPM": 3, "Nama": "NAMI", "Angkatan": 2008, "Alamat": "NATAR"}
]

# Fungsi untuk menampilkan data mahasiswa
def tampil_data():
    for mhs in mahasiswa:
        print("NPM:", mhs["NPM"], "Nama:", mhs["Nama"], "Angkatan:", mhs["Angkatan"], "Alamat:", mhs["Alamat"])
    print()

# Fungsi untuk menambah data mahasiswa baru
def tambah_data():
    npm = int(input("Masukkan NPM: "))
    nama = input("Masukkan Nama: ")
    angkatan = int(input("Masukkan Angkatan: "))
    alamat = input("Masukkan Alamat: ")
    mahasiswa.append({"NPM": npm, "Nama": nama, "Angkatan": angkatan, "Alamat": alamat})
    print("Data berhasil ditambahkan!")

# Fungsi untuk menghapus data mahasiswa berdasarkan NPM
def hapus_data():
    npm = int(input("Masukkan NPM mahasiswa yang ingin dihapus: "))
    for mhs in mahasiswa:
        if mhs["NPM"] == npm:
            mahasiswa.remove(mhs)
            print("Data mahasiswa dengan NPM", npm, "telah dihapus.")
            return
    print("Data mahasiswa tidak ditemukan.")

# Fungsi untuk mengupdate data mahasiswa berdasarkan NPM
def update_data():
    npm = int(input("Masukkan NPM mahasiswa yang ingin diupdate: "))
    for mhs in mahasiswa:
        if mhs["NPM"] == npm:
            mhs["Nama"] = input("Masukkan Nama baru: ")
            mhs["Angkatan"] = int(input("Masukkan Angkatan baru: "))
            mhs["Alamat"] = input("Masukkan Alamat baru: ")
            print("Data mahasiswa dengan NPM", npm, "telah diupdate.")
            return
    print("Data mahasiswa tidak ditemukan.")

# Main program
while True:
    print("Tampil Data Mahasiswa:")
    tampil_data()
    print("Pilih Menu:")
    print("1. Tambah Data Baru")
    print("2. Hapus Data by NPM")
    print("3. Update Data by NPM")
    print("4. Exit")
    menu = input("Pilih Menu: ")

    if menu == "1":
        tambah_data()
    elif menu == "2":
        hapus_data()
    elif menu == "3":
        update_data()
    elif menu == "4":
        break
    else:
        print("Menu tidak valid. Silakan pilih kembali.")

# Menampilkan data terakhir setelah melakukan operasi
print("Data Mahasiswa setelah Operasi:")
tampil_data()
