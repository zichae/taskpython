def myprime(p):
    if p > 1:
        for i in range(2,int(p/2)+1):
            if (p % i) == 0:
                print("nomor", p, "ini bukan prima")
                break
        else:
                print("nomor", p, "ini merupakan bilangan prima")
    else:
        print("nomor", p, "ini bukan prima")

p= int(input("Masukkan bilangan: "))
myprime(p)