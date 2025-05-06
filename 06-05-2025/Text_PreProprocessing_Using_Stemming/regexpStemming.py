from nltk.stem import RegexpStemmer
# It basically takes a single regular expression and removes any prefix or suffix that matches the expression

reg_exp = RegexpStemmer("ing$|s$|e$|able$", min=4)

print(reg_exp.stem("eating"))
print(reg_exp.stem("playing"))
print(reg_exp.stem("sleeping"))
print(reg_exp.stem("reading"))

print(reg_exp.stem("reads"))
print(reg_exp.stem("books"))


words = [
    "eating", "playing", "sleeping", "reading",   # -ing suffix
    "reads", "books", "tables", "classes",        # -s suffix
    "make", "bake", "hope",                       # -e suffix
    "enjoyable", "readable", "understandable",    # -able suffix
    "run", "go", "be", "do"                        # short or no-match words
]

reg_exp = RegexpStemmer("ing$|s$|e$|able$", min=4)

for word in words:
    print(reg_exp.stem(word))