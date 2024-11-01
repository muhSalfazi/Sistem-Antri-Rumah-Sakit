from collections import deque
from datetime import datetime
from prettytable import PrettyTable

class AntrianRumahSakit:
    """
    Kelas ini mengelola sistem antrian pasien di rumah sakit.
    
    Attributes:
    ----------
    antrian : deque
        Struktur data antrian yang menyimpan data pasien dalam urutan FIFO.
    nomor_antrian : int
        Nomor antrian yang akan diberikan ke pasien berikutnya.
    """

    def __init__(self):
        """
        Inisialisasi kelas AntrianRumahSakit.
        
        Mengatur antrian kosong dengan nomor antrian awal 1.
        """
        self.antrian = deque()
        self.nomor_antrian = 1

    def tambah_pasien(self, nama_pasien):
        """
        Menambahkan pasien baru ke dalam antrian.
        
        Parameters:
        ----------
        nama_pasien : str
            Nama pasien yang akan ditambahkan ke antrian.
        """
        waktu_kedatangan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.antrian.append((self.nomor_antrian, nama_pasien, waktu_kedatangan))
        print(f"Pasien '{nama_pasien}' ditambahkan dengan nomor antrian {self.nomor_antrian}.")
        self.nomor_antrian += 1

    def panggil_pasien(self):
        """
        Memanggil pasien pertama dalam antrian dan menghapusnya dari antrian.
        
        Menampilkan informasi pasien yang dipanggil.
        """
        if self.antrian:
            nomor_antrian, nama_pasien, waktu_kedatangan = self.antrian.popleft()
            print(f"Memanggil pasien dengan nomor antrian {nomor_antrian}: {nama_pasien} (Waktu Kedatangan: {waktu_kedatangan})")
        else:
            print("Tidak ada pasien dalam antrian.")

    def lihat_antrian(self):
        """
        Menampilkan daftar pasien dalam antrian dalam format tabel.
        
        Jika antrian kosong, menampilkan pesan yang sesuai.
        """
        if self.antrian:
            table = PrettyTable()
            table.field_names = ["Nomor Antrian", "Nama Pasien", "Waktu Kedatangan"]
            for nomor_antrian, nama_pasien, waktu_kedatangan in self.antrian:
                table.add_row([nomor_antrian, nama_pasien, waktu_kedatangan])
            print(table)
        else:
            print("Antrian kosong. Tidak ada pasien yang menunggu.")
