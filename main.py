from antrian import AntrianRumahSakit
from interface import proses_input

def main():
    """
    Fungsi utama untuk memulai aplikasi sistem antrian rumah sakit.
    
    Membuat objek AntrianRumahSakit dan memulai antarmuka pengguna untuk mengelola antrian.
    """
    antrian = AntrianRumahSakit()
    proses_input(antrian)

if __name__ == "__main__":
    main()
