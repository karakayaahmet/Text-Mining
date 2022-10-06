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

mdf = df.copy()

mdf = mdf["hikayeler"].str.replace("[^\w\s]","")

