string = ""

x = int(input("Masukkan angka: "))
bar = x
#looping baris
while bar >= 0:

    #looping kolom spasi kosong
    kol = bar
    while kol > 0:
        string = string + " "
        kol = kol - 1

    #looping kolom bintang
    kanan = 1
    while kanan < (x - (bar-1)):
        string = string + "*"
        kanan = kanan + 1

    string = string + "\n"
    bar = bar - 1

print (string) 