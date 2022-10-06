import pandas as pd

metin = """
A Scandal in Bohemia! 01
The Red-headed League,2
A Case, of Identity 33
The Boscombe Valley Mystery4
The Five Orange Pips1
The Man with? the Twisted Lip
The Adventure of the Blue Carbuncle
The Adventure of the Speckled Band
The Adventure of the Engineer's Thumb
The Adventure of the Noble Bachelor
The Adventure of the Beryl Coronet
The Adventure of the Copper Beeches"""

print(metin)
v = metin.split("\n")
seri = pd.Series(v)
df = pd.DataFrame(seri, columns=["hikayeler"])

cdf = df.copy()

list1 = [1,2,3]
str1 = "".join(str(i) for i in list1)
print(str1)

print(cdf["hikayeler"].apply(lambda x: " ".join(x.lower() for x in x.split())))

print(cdf["hikayeler"].apply(lambda x: " ".join(x.upper() for x in x.split())))