kendaraaan = ["Palisade", "mobil", "2199 CC", "4"]
kendaraaan.append ("875juta")
kendaraaan.append ("Palisade")
kendaraaan.insert (4,"Hyundai")
print (kendaraaan)

print (''' ''')


match pilihan:
    case '1':
        sisi = int(input(masukan sisi:))
        luas_p = sisi * sisi
        print('luas persegi kamu adalah ', luas_p)
    case '2':
        jari2=float(input('Masukan jari-jari:'))
        luas_L = 3.14*jari2*jari2
        print('luas lingkaran kamu adalah', int(luas_L))
    case '3':
        alas=int(input('masukan : '))
        tinggi=int(input('masukan ')) 
        luas_L = 3.14*jari2*jari2
        print('luas lingkaran kamu adalah ', int(luas_L))       
