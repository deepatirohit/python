# Snowball Stemmer (also known as Porter2 stemmer) is a more advanced stemming algorithm provided by the NLTK library. 
# It is designed to reduce words to their root forms (stems) in a linguistically accurate way, and supports multiple languages.

from nltk.stem import SnowballStemmer

snowball_stemmer = SnowballStemmer("english")

words = [
    "disconnect", "disagree", "dislike",
    "preview", "preheat", "preplan",
    "rewrite", "replay", "return",
    "biology", "geography", "photograph",
    "transmit", "transport", "transform",
    "circle", "apple", "keyboard", "run"
]

for word in words:
    print(word+" ---->" +snowball_stemmer.stem(word))
    
print(snowball_stemmer.stem("fairly"))
print(snowball_stemmer.stem("playing"))
print(snowball_stemmer.stem("sports"))