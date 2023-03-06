#input bilangan
x = int(input("masukkan angka: "))

angka_prima =  True
if((x == 0) or (x == 1)):
    angka_prima = False
else:
    for i in range (2, (x//2)):
      if x % i == 0:
         angka_prima = False
         break
    
if(angka_prima):
   print(x, "merupakan angka prima")
else:
   print(x,"bukan merupakan angka prima")
