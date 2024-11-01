from antrian import AntrianRumahSakit

def tampilkan_menu():
    """
    Menampilkan menu pilihan kepada pengguna.
    """
    print("\n--- Sistem Antrian Rumah Sakit ---")
    print("1. Tambah Pasien ke Antrian")
    print("2. Panggil Pasien")
    print("3. Lihat Daftar Antrian")
    print("4. Keluar")

def proses_input(antrian):
    """
    Mengelola input pengguna dan menjalankan fungsi sesuai pilihan pengguna.
    
    Parameters:
    ----------
    antrian : AntrianRumahSakit
        Objek kelas AntrianRumahSakit untuk mengelola operasi antrian.
    """
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1-4): ")
        
        if pilihan == '1':
            nama_pasien = input("Masukkan nama pasien: ")
            antrian.tambah_pasien(nama_pasien)
        elif pilihan == '2':
            antrian.panggil_pasien()
        elif pilihan == '3':
            antrian.lihat_antrian()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan sistem antrian.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
