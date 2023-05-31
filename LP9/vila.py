from hunian import Hunian

class Vila(Hunian):
    def __init__(self, nama_pemilik, gambar, lokasi, luastanah, nama_vila, jml_penghuni, jml_kamar):
        super().__init__("Vila", gambar, lokasi, luastanah, jml_penghuni, jml_kamar)
        self.nama_vila = nama_vila
        self.nama_pemilik = nama_pemilik
    
    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik
    
    def get_nama_vila(self):
        return self.nama_vila
    
    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_detail(self):
        return "Jumlah Kamar : " + str(self.jml_kamar) + "\nNama Vila : " + str(self.nama_vila) + "\n"
