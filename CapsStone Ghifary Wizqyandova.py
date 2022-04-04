dict_pasien = {"A01" : {"Nama" : "Ahmad",  "Domisili" : "Jakarta", "Sakit" : "Lambung", "Obat" : "Operasi"},
                "J02" : {"Nama" : "Joni",  "Domisili" : "Bandung", "Sakit" : "Mata", "Obat" : "Laser"}}

### Akses semua data
def semua_data():
    for i in dict_pasien:
        print("Data pasien {} bernama {} asal {} memiliki penyakit {}, Pengobatan {}".format(i,dict_pasien[i]["Nama"], dict_pasien[i]["Domisili"], dict_pasien[i]["Sakit"], dict_pasien[i]["Obat"]))
    read_data()

### Akses data tertentu
def data_spesifik():
    code = input("Masukkan ID Pasien : ").capitalize()
    if code in dict_pasien.keys():
        print("Data pasien {} bernama {} asal {} memiliki penyakit {}, Pengobatan {}".format(code,dict_pasien[code]["Nama"], dict_pasien[code]["Domisili"], dict_pasien[code]["Sakit"], dict_pasien[code]["Obat"]))
        read_data()
    else:
        print("Tidak Ada Data Pasien")
        read_data()

### Menu Read Data
def read_data():
    print("")
    print("======Report Data Pasien======")
    print("")
    print("1. Report Seluruh Pasien")
    print("2. Report Pasien Tertentu")
    print("3. Kembali Ke Menu Utama")
    pilih_menu = input("Silakan Masukan Angka 1-3 : ")
    if pilih_menu == ('1'):
        semua_data()
    elif pilih_menu == ('2'):
        data_spesifik()
    elif pilih_menu == ('3'):
        menu_utama()
    else:
        read_data()

### Create Data
def create_data():    
    global id_baru, data_baru
    data_baru = {}
    id_baru = input("Masukkan ID Pasien : ").capitalize()
    if id_baru in dict_pasien.keys():
        print("Data Sudah Ada")
        menu_create()
    else:
        global nama
        nama = input("Masukkan Nama : ").capitalize()
        data_baru["Nama"] = nama
        global domisili
        domisili = input("Masukkan Domisili : ").capitalize()
        data_baru["Domisili"] = domisili
        global sakit
        sakit = input("Masukkan Jenis Penyakit : ").capitalize()
        data_baru["Sakit"] = sakit
        global obat
        obat = input("Masukkan Jenis Pengobatan : ").capitalize()
        data_baru["Obat"] = obat
        simpan_data()

### Simpan Create Data
def simpan_data():
    simpan = input("Apakah Data akan disimpan? (Y/N) : ").capitalize()
    global dict_pasien
    if simpan == 'Y':
        print("Data Tersimpan")
        dict_pasien[id_baru] = data_baru
        menu_create()        
    elif simpan == 'N':
        dict_pasien = dict_pasien
        print("Data Pasien Tidak Tersimpan")
        menu_create()
    else:
        simpan_data()

    ### Menu Create
def menu_create():
    print("")
    print("======Menambah Data Pasien======")
    print("")
    print("1. Tambah Data Pasien")
    print("2. Kembali Ke Menu Utama")
    create_menu = input("Silakan Masukan Angka 1-2 : ")
    if create_menu == ('1'):
        create_data()
    elif create_menu == ('2'):
        menu_utama()
    else:
        menu_create()

#### Menu Update Data
def menu_update():
    print("")
    print("======Mengubah Data Pasien=====")
    print("")
    print("1. Ubah Data Pasien")
    print("2. Kembali Ke Menu Utama")
    update_menu = input("Silakan Masukan angka 1-2 : ")
    if update_menu == ('1'):
        check_data()
    elif update_menu == ('2'):
        menu_utama()
    else:
        menu_update()

### check update data
def check_data():
    global update_id
    update_id = input("Masukkan ID Pasien : ").capitalize()
    if update_id in dict_pasien:
        print("Data pasien {} bernama {} asal {} memiliki penyakit {}, Pengobatan {}".format(update_id, dict_pasien[update_id]["Nama"], dict_pasien[update_id]["Domisili"], dict_pasien[update_id]["Sakit"], dict_pasien[update_id]["Obat"]))
        update_data()
    else:
        print("Data Pasien Tidak Ditemukan!")
        menu_update()

### Check keterangan yg ingin di update        
def kolom_edit():
    update_key = input("Masukkan Pilihan yg ingin di ubah : ").capitalize()
    if update_key in dict_pasien[update_id]:
        data_ubah = input("Masukkan {} Baru : ".format(update_key)).capitalize()
        m = 1
        while m != 0:
            simpan_update = input("Apakah Data akan diupdate? (Y/N) : ").capitalize()
            if simpan_update == 'Y':
                dict_pasien[update_id][update_key] = data_ubah
                print("Data Updated")
                menu_update()
                m = 0
            elif simpan_update == 'N':
                print("Data Tidak Terupdate")
                menu_update()
                m = 0
            else:
                m = 1
    else:
        print("Mohon Masukkan Pilihan yang benar")
        kolom_edit()

### check update data
def update_data():
    pil_upd = input("Tekan Y jika ingin lanjut Update Data atau N jika ingin cancel Update : ").capitalize()
    if pil_upd == 'Y':
        kolom_edit()
    elif pil_upd == 'N':
        print("Data Tidak Terupdate")
        menu_update()
    else:
        update_data()

### Menu Delete Data
def menu_delete():
    print("")
    print("============Menghapus Data Pasien============")
    print("")
    print("1. Hapus Data Pasien")
    print("2. Kembali Ke Menu Utama")
    delete_menu = input("Silakan Masukan Angka 1-2 : ")
    if delete_menu == ('1'):
        delete_data()
    elif delete_menu == ('2'):
        menu_utama()
    else:
        menu_delete()

def delete_data():
    global delete_code
    delete_code = input("Masukkan ID Pasien : ").capitalize()
    if delete_code in dict_pasien.keys():
        delete_data_notif()
    else:
        print("Data Tidak Ada")
        menu_delete()

def delete_data_notif():
    hapus_data = input("Apakah data akan dihapus? (Y/N) : ").capitalize()
    if hapus_data == 'Y':
        print("Data Terhapus")
        dict_pasien.pop(delete_code)
        menu_delete()
    elif hapus_data == 'N':
        print("Data Tidak Terhapus")
        menu_delete()
    else:
        delete_data_notif()

def menu_utama():
    print("")
    print("==========Selamat Datang di Rumah Sakit Sehat Lagi==========")
    print("")
    print("1. Report Data Pasien")
    print("2. Tambah Data Pasien")
    print("3. Ubah Data Pasien")
    print("4. Hapus Data Pasien")
    print("5. Exit")
    main_menu = input("Silakan Masukan Angka 1-5 : ")
    if main_menu == ('1'):
        read_data()
    elif main_menu == ('2'):
        menu_create()
    elif main_menu == ('3'):
        menu_update()
    elif main_menu == ('4'):
        menu_delete()
    elif main_menu == ('5'):
        global exit
        exit = 0
        print("Terima Kasih dan selalu Sehat!!")
    else:
        print("====Pilihan yang anda masukkan salah====")
        menu_utama()
menu_utama()