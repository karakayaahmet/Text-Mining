import enum
from fnmatch import translate
from traceback import print_tb
import pandas as pd

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

print("a12".isalnum)

#Elemanlarına ve eleman indexlerine erişmek

isim = "mvk"

print(isim[0:2])

print(isim.index("v"))

#Başlangıç ve Bitiş Karakterlerini Sorgulamak.

m = "mustafa"

print(m.startswith("a"))

print(m.endswith("b"))

#Count

print(m.count("a"))

#Sorted 

print(sorted(m))

print(*sorted(m), sep="")

#Karakterleri Bölmek

print(m.split())

print(m.split("a"))

#Büyük Küçük Harf İşlemleri

print(m.lower())

print(m.upper())

print(m.upper().lower())

print(m.isupper())

print(m.islower())

#Capitalize, Title, Swapcase

print(m.capitalize())

print(m.title())

print(m.swapcase()) #Büyük olan karakterler küçük, küçük olan karakterler büyük olacak.

#İstenmeyen Karakterleri Kırpmak: strip(), lstrip(), rstrip()

s = " hello "

print(s.strip())

s = "**hello**"

print(s.strip("*"))

print(s.rstrip("*"))

print(s.lstrip("*"))

#Bölünmüş ya da Bölük Olan İfadelerin Birleştirilmesi

okul = "Firat Üniversitesi Yazilim Muhendisligi"

ayrik = okul.split()

print(ayrik)

joiner = " "

print(joiner.join(ayrik))

yildiz = "**"

print(yildiz.join(ayrik))

#Eleman Değiştirme: replace(), str.maketrans(), translate()

isim = "Kenan"

print(isim.replace("K","c"))

ifade = "bu ifadede bağzı türkçe karakterler vardır."

duzeltilecek_harfler = "çÇğĞiİüÜ"
duzeltilmis_harfler = "cCgGiİuU"

alfabe_duzelt = str.maketrans(duzeltilecek_harfler,duzeltilmis_harfler)
ifade.translate(alfabe_duzelt)

ifade = "Fırat Üniversitesi Yazılım Mühendisliği Programı Veri Madenciliği Dersi Kapsamında Yapılan Çalışmalar"

duzelticekler = "ıİüÜöÖşŞğĞçÇ"
duzeltilenler = "iIuUoOsSgGcC"

duzelt = ifade.maketrans(duzelticekler,duzeltilenler)
print(ifade)
print(ifade.translate(duzelt))

#Contains

isimler = ["ali","ayşe","fatma","nergis","burak","cem"]
seri = pd.Series(isimler)

print(seri)

print(seri.str.contains("al"))

print(seri[seri.str.contains("al")])

print(seri.str.contains("al").sum())

print(seri.str.contains("[aA]l").sum())