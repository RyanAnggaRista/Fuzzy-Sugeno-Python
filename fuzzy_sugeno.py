class Fuzzy:
    def __init__(self, jarak, zona_kasus):
        self.jarak = jarak
        self.zona_kasus = zona_kasus

    def Fuzzyfikasi(self):
        # sangat bahaya
        if self.jarak <= 40:
            self.nilai_keanggotaan_sangat_bahaya = 1
        elif self.jarak > 40 and self.jarak < 50:
            self.nilai_keanggotaan_sangat_bahaya = (
                50 - self.jarak) / (50 - 40)
        elif self.jarak >= 50:
            self.nilai_keanggotaan_sangat_bahaya = 0

        # bahaya
        if self.jarak > 40 and self.jarak < 50:
            self.nilai_keanggotaan_bahaya = (self.jarak - 40) / (50 - 40)
        elif self.jarak == 50:
            self.nilai_keanggotaan_bahaya = 1
        elif self.jarak > 50 and self.jarak < 60:
            self.nilai_keanggotaan_bahaya = (60 - self.jarak) / (60 - 50)
        elif self.jarak <= 40 or self.jarak >= 60:
            self.nilai_keanggotaan_bahaya = 0

        # awas
        if self.jarak > 50 and self.jarak < 60:
            self.nilai_keanggotaan_awas = (self.jarak - 50) / (60 - 50)
        elif self.jarak == 60:
            self.nilai_keanggotaan_awas = 1
        elif self.jarak > 60 and self.jarak < 70:
            self.nilai_keanggotaan_awas = (70 - self.jarak) / (70 - 60)
        elif self.jarak <= 50 or self.jarak >= 70:
            self.nilai_keanggotaan_awas = 0

        # Warning
        if self.jarak > 60 and self.jarak < 70:
            self.nilai_keanggotaan_warning = (self.jarak - 60) / (70 - 60)
        elif self.jarak == 70:
            self.nilai_keanggotaan_warning = 1
        elif self.jarak > 70 and self.jarak < 80:
            self.nilai_keanggotaan_warning = (80 - self.jarak) / (80 - 70)
        elif self.jarak <= 60 or self.jarak >= 80:
            self.nilai_keanggotaan_warning = 0

        # Peringatan
        if self.jarak <= 70:
            self.nilai_keanggotaan_peringatan = 0
        elif self.jarak > 70 and self.jarak < 80:
            self.nilai_keanggotaan_peringatan = (self.jarak - 70) / (80 - 70)
        elif self.jarak >= 80:
            self.nilai_keanggotaan_peringatan = 1

        # Tidak berwarna
        if self.zona_kasus <= 0.5:
            self.nilai_keanggotaan_zona_tidak_berwarna = 1
        elif self.zona_kasus > 0.5 and self.zona_kasus < 1:
            self.nilai_keanggotaan_zona_tidak_berwarna = (
                1 - self.zona_kasus) / (1 - 0.5)
        elif self.zona_kasus >= 1:
            self.nilai_keanggotaan_zona_tidak_berwarna = 0

        # Kuning
        if self.zona_kasus > 0.5 and self.zona_kasus <= 1:
            self.nilai_keanggotaan_zona_kuning = (
                self.zona_kasus - 0.5) / (1 - 0.5)
        elif self.zona_kasus == 1:
            self.nilai_keanggotaan_zona_kuning = 1
        elif self.zona_kasus > 1 and self.zona_kasus < 1.5:
            self.nilai_keanggotaan_zona_kuning = (
                1.5 - self.zona_kasus) / (1.5 - 1)
        elif self.zona_kasus <= 0.5 or self.zona_kasus >= 1.5:
            self.nilai_keanggotaan_zona_kuning = 0

        # Merah
        if self.zona_kasus <= 1:
            self.nilai_keanggotaan_zona_merah = 0
        elif self.zona_kasus > 1 and self.zona_kasus < 2:
            self.nilai_keanggotaan_zona_merah = (self.zona_kasus - 1) / (2 - 1)
        elif self.zona_kasus >= 2:
            self.nilai_keanggotaan_zona_merah = 1
            
    def RuleBase(self):
        self.a1 = min(self.nilai_keanggotaan_sangat_bahaya, self.nilai_keanggotaan_zona_tidak_berwarna)
        self.a2 = min(self.nilai_keanggotaan_bahaya,
                      self.nilai_keanggotaan_zona_kuning)
        self.a3 = min(self.nilai_keanggotaan_awas,
                      self.nilai_keanggotaan_zona_merah)
        self.a4 = min(self.nilai_keanggotaan_warning,
                      self.nilai_keanggotaan_zona_tidak_berwarna)
        self.a5 = min(self.nilai_keanggotaan_peringatan,
                      self.nilai_keanggotaan_zona_kuning)
        self.a6 = min(self.nilai_keanggotaan_sangat_bahaya,
                      self.nilai_keanggotaan_zona_merah)
        self.a7 = min(self.nilai_keanggotaan_bahaya,
                      self.nilai_keanggotaan_zona_tidak_berwarna)
        self.a8 = min(self.nilai_keanggotaan_awas,
                      self.nilai_keanggotaan_zona_kuning)
        self.a9 = min(self.nilai_keanggotaan_warning,
                      self.nilai_keanggotaan_zona_merah)
        self.a10 = min(self.nilai_keanggotaan_peringatan,
                       self.nilai_keanggotaan_zona_tidak_berwarna)
        self.a11 = min(self.nilai_keanggotaan_sangat_bahaya,
                       self.nilai_keanggotaan_zona_kuning)
        self.a12 = min(self.nilai_keanggotaan_bahaya,
                       self.nilai_keanggotaan_zona_merah)
        self.a13 = min(self.nilai_keanggotaan_awas,
                       self.nilai_keanggotaan_zona_tidak_berwarna)
        self.a14 = min(self.nilai_keanggotaan_warning,
                       self.nilai_keanggotaan_zona_kuning)
        self.a15 = min(self.nilai_keanggotaan_peringatan,
                       self.nilai_keanggotaan_zona_merah)

    def Defuzzyfikasi(self):
        # perhitungan rule
        self.jumlah = (self.a1+self.a2 + self.a3 + self.a4 + self.a5 + self.a6 + self.a7 +
                       self.a8 + self.a9 + self.a10 + self.a11 + self.a12 + self.a13 + self.a14 + self.a15)
        self.lampu_merah = ((self.a1 * 0) + (self.a2 * 1) + (self.a3 * 0) + (self.a4 * 0) + (self.a5 * 0) + (self.a6 * 1) + (self.a7 * 0) + (self.a8 * 0) +
                            (self.a9 * 0) + (self.a10 * 0) + (self.a11 * 1) + (self.a12 * 1) + (self.a13 * 0) + (self.a14 * 0) + (self.a15 * 0)) / self.jumlah
        self.lampu_kuning = ((self.a1 * 0) + (self.a2 * 0) + (self.a3 * 1) + (self.a4 * 0) + (self.a5 * 1) + (self.a6 * 0) + (self.a7 * 0) + (self.a8 * 1) +
                             (self.a9 * 1) + (self.a10 * 0) + (self.a11 * 0) + (self.a12 * 0) + (self.a13 * 0) + (self.a14 * 1) + (self.a15 * 1)) / self.jumlah
        self.suara_1 = ((self.a1 * 0) + (self.a2 * 0) + (self.a3 * 0) + (self.a4 * 0) + (self.a5 * 0) + (self.a6 * 0) + (self.a7 * 0) + (self.a8 * 0) +
                        (self.a9 * 1) + (self.a10 * 0) + (self.a11 * 0) + (self.a12 * 0) + (self.a13 * 0) + (self.a14 * 1) + (self.a15 * 0)) / self.jumlah
        self.suara_2 = ((self.a1 * 0) + (self.a2 * 0) + (self.a3 * 1) + (self.a4 * 0) + (self.a5 * 0) + (self.a6 * 0) + (self.a7 * 0) + (self.a8 * 1) +
                        (self.a9 * 0) + (self.a10 * 0) + (self.a11 * 0) + (self.a12 * 0) + (self.a13 * 0) + (self.a14 * 0) + (self.a15 * 0)) / self.jumlah
        self.suara_3 = ((self.a1 * 0) + (self.a2 * 0) + (self.a3 * 0) + (self.a4 * 0) + (self.a5 * 0) + (self.a6 * 1) + (self.a7 * 0) + (self.a8 * 0) +
                        (self.a9 * 0) + (self.a10 * 0) + (self.a11 * 1) + (self.a12 * 0) + (self.a13 * 0) + (self.a14 * 0) + (self.a15 * 0)) / self.jumlah 
    
    def Print(self):
        print("_____FUZZY SUGENO_____")
        print("Input Jarak = ", self.jarak)
        print("Input Zona Kasus = ", self.zona_kasus)
        print("_____PROSES FUZZYFIKASI_____")
        print("Nilai Keanggotaan Sangat Bahaya = ", self.nilai_keanggotaan_sangat_bahaya)
        print("Nilai Keanggotaan Bahaya = ", self.nilai_keanggotaan_bahaya)
        print("Nilai Keanggotaan Awas = ", self.nilai_keanggotaan_awas)
        print("Nilai Keanggotaan Warning = ", self.nilai_keanggotaan_warning)
        print("Nilai Keanggotaan Peringatan = ", self.nilai_keanggotaan_peringatan)
        print("Nilai Keanggotaan Zona Tidak Berwarna = ", self.nilai_keanggotaan_zona_tidak_berwarna)
        print("Nilai Keanggotaan Zona Kuning = ", self.nilai_keanggotaan_zona_kuning)
        print("Nilai Keanggotaan Zona Merah = ", self.nilai_keanggotaan_zona_merah)
        print("_____PROSES RULEBASE_____")
        print("a1 = ", self.a1)
        print("a2 = ", self.a2)
        print("a3 = ", self.a3)
        print("a4 = ", self.a4)
        print("a5 = ", self.a5)
        print("a6 = ", self.a6)
        print("a7 = ", self.a7)
        print("a8 = ", self.a8)
        print("a9 = ", self.a9)
        print("a10 = ", self.a10)
        print("a11 = ", self.a11)
        print("a12 = ", self.a12)
        print("a13 = ", self.a13)
        print("a14 = ", self.a14)
        print("a15 = ", self.a15)
        print("_____PROSES DEFUZZYFIKASI_____")
        print("Lampu Merah = ", self.lampu_merah)
        print("Lampu Kuning = ", self.lampu_kuning)
        print("Suara 1 = ", self.suara_1)
        print("Suara 2 = ", self.suara_2)
        print("Suara 3 = ", self.suara_3)

def main():
    input = Fuzzy(54, 1)
    input.Fuzzyfikasi()
    input.RuleBase()
    input.Defuzzyfikasi()
    input.Print()

if __name__ == "__main__":
    main()
