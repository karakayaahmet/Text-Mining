import pandas as pd
from nltk.stem import PorterStemmer
import nltk
nltk.download("punkt")
from textblob import TextBlob
import textblob

st = PorterStemmer

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

a = df["hikayeler"].apply(lambda x: " ".join(st.stem(i) for i in x.split()))
print(a)

