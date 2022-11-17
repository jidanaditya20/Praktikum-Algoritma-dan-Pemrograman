#Tugas Akhir Pratikum Algoritma Pemrograman
# Kasir Makanan

pilihan ="y"
while pilihan =="y":
    print("""
    ==============================
    Selamat datang di SEBLAK GAZZ
    List Menu Makanan dan Minuman
    
    ==============================
    1. Seblak B Aja : Rp 10.000
    2. Seblak Lumayan Aja : Rp 13.000
    3. Seblak Gazz Tross Level Max : Rp 15.000
    4. Thai Tea : Rp 8.000
    5. Lemon Tea : Rp 8.000
    6. Tropical Blue Mango : Rp 13.000
    ===============================
    """ )
    namapelanggan=str(input("Masukan Nama Anda :"))
    alamat=str(input("Masukkan Alamat Anda :"))
    notelepon=str(input("Masukkan No Telepon Anda :"))
    tanggal=str(input("Masukkan Tanggal Pembelian :"))
    pesan=str(input("Masukkan List No Menu Seblak :"))
    jumlahpesan=int(input("Masukkan Jumlah Pesanan :"))
    if pesan =="1":
        listnama="Seblak B Aja"
        harga=(10000*jumlahpesan)
        totalharga = int(harga*jumlahpesan)
    elif pesan =="2":
        listnama="Seblak Lumayan Aja"
        harga=(13000*jumlahpesan)
        totalharga = int(harga*jumlahpesan)
    elif pesan =="3":
        listnama="Seblak Gazz Tross Level Max"
        harga=(15000*jumlahpesan)
        totalharga = int(harga*jumlahpesan)
    elif pesan =="4":
        listnama="Thai Tea"
        harga=(8000*jumlahpesan)
        totalharga = int(harga*jumlahpesan)
    elif pesan =="5":
        listnama=("Lemon Tea")
        harga=(8000*jumlahpesan)
        totalharga = int(harga*jumlahpesan)
    elif pesan =="6":
        listnama=("Tropical Blue Mango")
        harga=(13000*jumlahpesan)
        totalharga = int(harga*jumlahpesan)
    else:
        namapelanggan = "-"
        alamat = "-"
        notelepon = "-"
        tanggal = "-"
        listnama = "-"
        harga = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan no menu yang tersedia silahkan ulangi kembali Y/N")

    print("--------------------------")
    print("SEBLAK GAZZ")
    print("--------------------------")
    print("Nama Pelanggan :",namapelanggan)
    print("Alamat :",alamat)
    print("No Telepon :",notelepon)
    print("Tanggal :",tanggal)
    print("Menu :",listnama)
    print("Jumlah Pesan :",jumlahpesan)
    print("Harga :",harga)
    print("--------------------------")
    print("Jumlah Bayar :",totalharga)
    print("--------------------------")
    pilihan=input("Apakah anda ingin memesan kembali Y/N :")

