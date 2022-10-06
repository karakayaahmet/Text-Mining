import enum
from traceback import print_tb

#Oluşturma Biçimlendirme

isim = "mvk"
print(3*isim)

print("mvk"+"ali")

print("K"+isim[1:])

isimler = ["ali","ayşe","fatma"]

for i in isimler:
    print("isim: ", i, sep="_")

print(*enumerate(isimler))

for i in enumerate(isimler):
    print(i)

for i in enumerate("isimler"):
    print(i)

for i in enumerate(isimler, 4):
    print(i)

#Dizi İçi Tip Sorgulamaları

print("mvk".isalpha)

print("mvk2".isalpha)

print("123".isnumeric)

print("234".isdigit)




