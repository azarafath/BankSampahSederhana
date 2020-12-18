#BANK SAMPAH UTS ALGORITMA DAN PEMOGRAMAN
#NAMA : AHMAD ZAKARIA FATHONI
#NIM  : 3.34.20.4.01
#KELAS: IK-1E
import pandas as pd

# inisialisasi class
class BankSampah():
    
    def __init__(self):
        self.data =[]
        self.jumlah = 0
        
    def tambahdata(self, nama, jenis, berat):

        self.data.append({'Nama':nama,
                    'Jenis':jenis,
                    'Berat':berat})
        self.jumlah += 1
            
    def Admin(self):
        print("Selamat Datang di Portal Data Admin")
        username = str(input("Masukkan Uername :"))
        password = str(input("Masukkan Password :"))
        if(username=="Ahmad" and password=='281201') :
          df = pd.DataFrame(self.data)
          print("="*50)
          print("Data Bank Sampah".center(50,' '))
          print("="*50)
          print(df)
          print("="*50)
          print()
        else:
          print("Username atau Password Salah!")
        
        
# function
def pilihan():
    print("="*50)
    print("Selamat Datang di Sistem Bank Sampah".center(50,' '))
    print("="*50)
    print("1. Setor Sampah(Nasabah)")
    print("2. Login Admin")
    print("3. Keluar")
    print("="*50)
    
    pilih = int(input("Masukkan pilihan : "))
    
    print()
    return pilih

def setor():
    print("Masukkan Nama Nasabah , Jenis Sampah dan Berat Setor")
    nama = input("Masukkan nama anda\t\t\t: ")
    print("="*50)
    print("Jenis Sampah | 1. Plastik | 2. Besi | 3. Kaca")
    print("="*50)
    jenis = input("Masukkan jenis (1/2/3)\t\t: ")
    berat = input("Masukkan berat *kg \t\t: ")
    
    BS.tambahdata(nama, jenis, berat)
    print()
        
# main program
BS = BankSampah()
pilih = 0
while (pilih != 3):
    pilih = pilihan()
    
    if (pilih == 1):
        setor()
        
    elif (pilih == 2):
        BS.Admin()
        
    elif (pilih == 3):
        print("Keluar dari program!")
        
    else:
        print("Tidak ada pilihan!")
        print()
