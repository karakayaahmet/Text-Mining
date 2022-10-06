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

a = pd.Series(" ".join(df["hikayeler"]).split()).value_counts()
print(a)

sil = a[-3:]
print(sil)

y = df["hikayeler"].apply(lambda x: " ".join(x for x in x.split() if x not in sil))

print(y)