# antrian.py
from collections import deque
from datetime import datetime
from prettytable import PrettyTable

class AntrianRumahSakit:
    def __init__(self):
        self.antrian = deque()
        self.nomor_antrian = 1

    def tambah_pasien(self, nama_pasien):
        """Menambahkan pasien ke dalam antrian dengan waktu kedatangan."""
        waktu_kedatangan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.antrian.append((self.nomor_antrian, nama_pasien, waktu_kedatangan))
        print(f"Pasien '{nama_pasien}' dengan nomor antrian {self.nomor_antrian} telah ditambahkan pada {waktu_kedatangan}.")
        self.nomor_antrian += 1

    def panggil_pasien(self):
        """Memanggil pasien pertama di antrian."""
        if self.antrian:
            nomor, pasien, waktu_kedatangan = self.antrian.popleft()
            print(f"Memanggil Pasien: Nomor {nomor}, Nama: {pasien}, Waktu Kedatangan: {waktu_kedatangan}")
        else:
            print("Antrian kosong. Tidak ada pasien yang menunggu.")

    def lihat_antrian(self):
        """Menampilkan daftar antrian saat ini dengan tampilan tabel."""
        if self.antrian:
            print("\nDaftar Antrian Saat Ini:")
            table = PrettyTable()
            table.field_names = ["Nomor Antrian", "Nama Pasien", "Waktu Kedatangan"]
            for nomor, pasien, waktu in self.antrian:
                table.add_row([nomor, pasien, waktu])
            print(table)
        else:
            print("Antrian kosong. Tidak ada pasien yang menunggu.")
