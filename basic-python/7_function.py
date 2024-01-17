# def <nama_fungsi>(parameters):
#     Kode

def full_name(first: str, last: str):
  return first + last

print(full_name("Danang", "Bahari"))

def customer(*args):
  return args

customer_list = customer('Danang', 'Bahari', 'Dimas', 'Bagus')
print(customer_list)

def person(**person_data):
  print(person_data)

person(name= 'Danang', age= 10)

# LAMBDA
# lambda <parameters> : <expression>

profit = lambda pendapatan, pengeluaran: pendapatan - pengeluaran
print(profit(1200000, 935000))

# CASE 1
"""
Buatlah sebuah fungsi **penghasilan_pegawai** yang dapat
menampung input dari user yang berisi apakah user merupakan pegawai **Tetap / Kontrak**
dan berapa jumlah jam lembur yang dilakukan oleh user.
"""

def calculate_extra_work_hour(employment_type: str, hour: int):
  PERMANENT_PER_HOUR = 50000
  CONTRACT_PER_HOUR = 30000

  final_hour = 0

  if hour < 0:
    return 0
  elif hour > 20 or hour < 20:
    final_hour = hour
  
  if employment_type.lower() == 'tetap':
    return PERMANENT_PER_HOUR * final_hour
  else:
    return CONTRACT_PER_HOUR * final_hour

def employee_salary(employment_type: str, extra_time: float):
  available_job = ['tetap', 'kontrak']
  PERMANENT_SALARY = 4500000
  CONTRACT_SALARY = 0.7 * PERMANENT_SALARY

  if employment_type.lower() not in available_job:
    print("Tidak Ada Tipe Pegawai Tersebut")
    return

  if extra_time < 0:
    print('Waktu Lembur tidak boleh kurang dari 0 atau bernilai negatif')
    return

  final_salary = 0

  if employment_type.lower() == 'tetap':
    final_salary += PERMANENT_SALARY
  else:
    final_salary += CONTRACT_SALARY
  
  extra_work_hour_salary = calculate_extra_work_hour(employment_type, extra_time)
  total_salary = final_salary + extra_work_hour_salary
  tax = 0.01 * total_salary

  print(f'Total Gaji Lembur: Rp.{extra_work_hour_salary}')
  print(f'Pajak Yang Harus dibayar: Rp.{tax}')
  print(f'Pendapatan: Rp.{total_salary - tax}')


employment_type = input("Kategori Pegawai (Tetap/Kontrak) : ")
extra_time = input("Berapa jam lembur : ")

employee_salary(employment_type, int(extra_time))

# CASE 2
"""
Dalam suatu program perhitungan geometri yang akan dibangun programmer, 
terdapat sebuah list yang berisikan nilai integer

1. Kemudian, agar program dapat melakukan perhitungan ratio, 
maka dibuatlah fungsi baru yang dapat menghitung ratio dari jumlah bilangan positif, 
negatif dan nol terhadap banyaknya elemen yang ada di dalam list, dengan ketelitian hingga 3 angka di belakang koma.
"""

def count_ratio(list):
  counter = {
    'positive': 0,
    'negative': 0,
    'nol': 0
  }

  for num in list:
    if num == 0:
      counter['nol'] += 1
    elif num < 0:
      counter['negative'] += 1
    elif num > 0:
      counter['positive'] += 1
  
  total_data = len(list)

  for data in counter:
    ratio = counter[data] / total_data
    print(f'Jumlah ratio bilangan {data}: {ratio:.3f}')

count_ratio([10, 8, 6, 4, 2, 0, -2, -4 ])


# CASE 3
"""
Perhitungan produk yang dibeli setelah dipotong diskon

Sebuah platform belanja online sedang mengadakan promo akhir tahun, 
dengan memberikan voucher diskon 40% untuk setiap total produk yang dibeli.
"""

def promo_price_list(*price):
  total_price = sum(price)
  total_discount = 0.45 * total_price
  total_paid = int(total_price - total_discount)
  return total_paid

total = promo_price_list(20000, 30000, 50000, 100000, 150000, 275000)
print(f'Total yang dibayarkan: Rp.{total}')