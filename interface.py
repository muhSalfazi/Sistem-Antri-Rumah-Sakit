# interface.py
from antrian import AntrianRumahSakit

def tampilkan_menu():
    print("\n=== Sistem Antrian Rumah Sakit ===")
    print("1. Tambah Pasien")
    print("2. Panggil Pasien")
    print("3. Lihat Antrian")
    print("4. Keluar")

def proses_input(antrian):
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == "1":
            nama_pasien = input("Masukkan nama pasien: ")
            antrian.tambah_pasien(nama_pasien)
        elif pilihan == "2":
            antrian.panggil_pasien()
        elif pilihan == "3":
            antrian.lihat_antrian()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem antrian rumah sakit.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
