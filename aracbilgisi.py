class Arac:
    def __init__(self,marka,model):
        self.marka=marka
        self.model=model
    def bilgi(self):
        print(f"Marka: {self.marka}, Model:{self.model}")
class Araba(Arac):
    def __init__(self,marka,model,kapiSayisi):
        super().__init__(marka,model)
        self.kapiSayisi=kapiSayisi
    def arabaBilgisi(self):
        self.bilgi()
        print(f"kapı sayısı: {self.kapiSayisi}")
benimArabam=Araba("Toyota","Corolla",4)
benimArabam.arabaBilgisi()
