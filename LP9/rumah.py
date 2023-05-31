from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, gambar, lokasi, luastanah, jml_penghuni, jml_kamar, lahanparkir):
        super().__init__("Rumah", gambar, lokasi, luastanah, jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.lahanparkir = lahanparkir

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik
    
    def get_lahanparkir(self):
        return self.lahanparkir

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_detail(self):
        return "Jumlah Kamar : " + str(self.jml_kamar) + "\nLahan Parkir : " + str(self.lahanparkir) + "\n"