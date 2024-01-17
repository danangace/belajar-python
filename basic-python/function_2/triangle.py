def area():
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    hitung = alas * tinggi / 2
    print(f'Luas Segitiga adalah: {hitung}')

def perimeter():
    sisi_1 = float(input("Masukkan sisi 1: "))
    sisi_2 = float(input("Masukkan sisi 2: "))
    sisi_3 = float(input("Masukkan sisi 3: "))
    hitung = sisi_1 + sisi_2 + sisi_3
    print(f'Keliling Segitiga adalah: {hitung}')