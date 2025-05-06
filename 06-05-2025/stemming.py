from nltk.stem import PorterStemmer

# Stemming is the process of reducing a word to its base or root form by removing prefixes or suffixes

words = [
    "disconnect", "disagree", "dislike",
    "preview", "preheat", "preplan",
    "rewrite", "replay", "return",
    "biology", "geography", "photograph",
    "transmit", "transport", "transform",
    "circle", "apple", "keyboard", "run"
]

stemming = PorterStemmer()

for word in words:
    print(word +"-----" +stemming.stem(word))
    


words = [
    "connect", "connected", "connecting", "connection", "programming", "programs",
    "agree", "agreed", "agreeing", "agreement",
    "play", "playing", "played", "playfully",
    "run", "running", "runner", "runs"
]

stemmer = PorterStemmer()

for word in words:
    print(f"{word:<12} --> {stemmer.stem(word)}")

stemmer = PorterStemmer()

print(stemmer.stem("Sitting"))
print(stemmer.stem("eating"))
print(stemmer.stem("playing"))
print(stemmer.stem("bathing"))
print(stemmer.stem("sleeping"))
