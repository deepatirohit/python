from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize, TreebankWordTokenizer


# corpus --> paragraph
# documents --> sentences
# vocabulary  --> Unique words present in the paragraph
# Words --> words present in the corpus

corpus = """
In VS Code, you can use Python files like Jupyter notebooks by adding special cell markers.
With the Jupyter extension, VS Code treats Python scripts almost like notebooks.
"""
print(corpus)
documents = sent_tokenize(corpus)

for sentence in documents:
    print(sentence)

words = word_tokenize(corpus)
print(words)

for word in words:
    print(word)

print(wordpunct_tokenize(corpus))

tokenizer = TreebankWordTokenizer()

print(tokenizer.tokenize(corpus))