# PRINTING
print("Hello World")
print('Saya sedang melakukan belajar printing')


# EXERCISE PRINTING

# Perusahaan A mendapatkan profit sebesar 20.000 usd di bulan Maret.
# Cobalah print angka besar profit yang didapatkan perusahaan A!
print(20000)
print(20_000)

# VARIABLE
# variable_name = <value>

name = "danang"

# bad naming variable
# Nama variabel terlalu pendek
# Nama variabel tidak dapat menggambarkan isi dari variabel
# Nama Variabel Diawali dengan angka
# Nama Variabel terdapat dengan simbol
# Nama variabel sama antara variabel 1 dan variabel 2

# good naming variable
# Jelas dan ringkas.
# Menggambarkan isi dari variabel.
# Bukan merupakan keyword yang ada python, seperti for, True, False, and, if, or else.
# Tidak mengandung karakter ataupun simbol khusus, termasuk spasi.
# Variabel hanya boleh diawali underscore (_) atau huruf.

age = 21
date = 8
month = 9
year = 2003

# PRINTING VARIABLE
# Ada dua cara atau style formatting di Python
# 1. style lama (menggunakan tanda persen %)
# 2. style baru (menggunakan metode format())

print("Hello my name is %s. I'm %s years old" %(name, age))

# ESCAPING STRING USING backslash
print(f'Hello my name is {name}. I\'m {age} years old')

# EXERCISE
chicken = 5000
spice = 10000
rice = 50000
total_expenditure = 65000

print(f'Harga ayam adalah Rp{chicken}')
print(f'Harga bumbu adalah Rp{spice}')
print(f'Harga beras adalah Rp{rice}')
print(f'Total belanjaan adalah Rp{total_expenditure}')

