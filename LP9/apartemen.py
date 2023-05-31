from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, gambar, lokasi, luastanah, jml_penghuni, jml_kamar, fasilitas):
        super().__init__("Apartemen", gambar, lokasi, luastanah, jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.fasilitas = fasilitas

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_fasilitas(self):
        return self.fasilitas
    
    def get_detail(self):
        return "Jumlah Kamar : " + str(self.jml_kamar) + "\nFasilitas : " + str(self.fasilitas) + "\n"