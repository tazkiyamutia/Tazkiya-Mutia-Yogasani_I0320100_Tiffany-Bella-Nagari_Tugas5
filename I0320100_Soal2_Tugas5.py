# Soal 2 Tugas 5

nama = input('Masukkan nama anda : ' )
nilai = int(input('Masukkan nilai anda : ' ))
nilai_huruf = None
if nilai <60:
   nilai_huruf = 'E'
elif nilai <64:
   nilai_huruf = 'C'
elif nilai <69:
   nilai_huruf = 'C+'
elif nilai <74:
   nilai_huruf = 'B'
elif nilai <79:
   nilai_huruf = 'B+'
elif nilai <84:
   nilai_huruf = 'A-'
else:
   nilai_huruf = 'A'

print('Halo,' , nama, '! Nilai anda setelah dikonversi adalah', nilai_huruf)