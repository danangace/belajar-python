import circle
import rectangle
import triangle

def main():
  shape = input("Apa yang ingin Hitung (lingkaran/persegi panjang/segitiga) :")
  type = input("luas/keliling: ")

  if shape.lower() == 'lingkaran':
    if type == 'luas':
      circle.area()
    else:
      circle.circumference()
  elif shape.lower() == 'persegi panjang':
    if type == 'luas':
      rectangle.area()
    else:
      rectangle.perimeter()
  elif shape.lower() == 'segitiga':
    if type == 'luas':
      triangle.area()
    else:
      triangle.perimeter()
  else:
    print('Operasi salah')


main()