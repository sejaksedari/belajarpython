

# impor fungsi dan variabel secara TIDAK SPESIFIK dari modul dcoding_hello
print("impor modul saja tanpa fungsi dan variabel = TIDAK SPESIFIK")
import dcoding_hello

persegi_panjang_pertama = dcoding_hello.mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

print(dcoding_hello.nama) #manggil variabel nama dari dcoding_hello.py
# Terlihat pada kode di atas bahwa untuk menampilkan variabel kita tidak menggunakan kurung tutup "()" seperti pada saat pemanggilan fungsi. Namun, kita tetap menggunakan "hello" sebagai modul yang telah kita impor sebelumnya.



# impor fungsi dan variabel secara SPESIFIK dari modul dcoding_hello
print("\nimpor fungsi dan variabel = SPESIFIK")
from dcoding_hello import mencari_luas_persegi_panjang, nama

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

print(nama) #manggil variabel nama dari dcoding_hello.py tapi GA PERLU pake nama modulnya sebelum nama variabel