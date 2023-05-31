class Hunian():
    def __init__(self, jenis, gambar, lokasi, luastanah, jml_penghuni = 1, jml_kamar = 1):
        self.jenis = jenis
        self.gambar = gambar
        self.lokasi = lokasi
        self.luastanah = luastanah
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar

    def get_jenis(self):
        return self.jenis
    
    def get_gambar(self):
        return self.gambar
    
    def get_lokasi(self):
        return self.lokasi
    def get_luastanah(self):
        return self.luastanah

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Lokasi : " + str(self.lokasi) + "\nHunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang."