import sympy as sp
import scipy.integrate as spi
import numpy as np

print("Masukkan fungsi : ")
a = input()

print(f"∫ {a} dx")

x = sp.Symbol('x')

hasil = sp.integrate(eval(a), x)

print(f"Integralna = {hasil} + k")

print("Masukkan batas awal : ")
p = int(input())
  
print("Masukkan batas akhir : ")
q = int(input())

integrand = lambda x  : eval(a)

result, error = spi.fixed_quad(integrand, p, q)
print('Result is ', result, 'with error ', error)
