#definisiin
string = ""
bar = 1
#input
x = int(input("masukkan angka: "))
#inisiasi var baru
while bar <= x:
    kol = bar
#looping 
    while kol > 0:
        string = string + "*"
        kol = kol - 1

    string = string + "\n"
    bar = bar + 1
print(string)