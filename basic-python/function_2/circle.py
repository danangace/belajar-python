from math import pi

def area():
  r=float(input("Masukkan jari-jari lingkaran: "))
  area = pi*r*r
  print(f'Luas Lingkaran adalah: {area:.2f}')

def circumference():
  r=float(input("Masukkan jari-jari lingkaran: "))
  circumference = 2*pi*r
  print(f'Keliling Lingkaran adalah: {circumference}')