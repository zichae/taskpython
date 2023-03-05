def fibonacci(n):
    if n < 1:
        return[n]
    list = fibonacci(n-1)
    angka1 = list[-2] if len(list) > 2 else 0
    angka2 = list[-1] if len(list) > 2 else 1
    return list + [angka1 + angka2]

panjang = int(input("Masukkan angka deret: "))
print(fibonacci(panjang-1))