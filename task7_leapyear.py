x = int(input("masukkan tahun: "))

if x % 400 == 0:
    print ( x, " merupakan tahun kabisat.")
elif x % 100 == 0:
    print (x, " bukan merupakan tahun kabisat.")
elif x % 4 == 0:
    print (x, " merupakan tahun kabisat.")
else:
    print (x, "bukan merupakan tahun kabisat.")