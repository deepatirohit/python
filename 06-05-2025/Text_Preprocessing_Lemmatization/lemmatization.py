from nltk.stem import WordNetLemmatizer
# examples: Q&A, chatbots, text, summarzation.

words = [
    "disconnect", "disagree", "dislike",
    "preview", "preheat", "preplan",
    "rewrite", "replay", "return",
    "biology", "geography", "photograph",
    "transmit", "transport", "transform",
    "circle", "apple", "keyboard", "run"
]

lemmatization = WordNetLemmatizer()

for word in words:
    print(lemmatization.lemmatize(word))
    
print(lemmatization.lemmatize("playing"))
print(lemmatization.lemmatize("plays"))    
print(lemmatization.lemmatize("played"))     
print(lemmatization.lemmatize("better"))     
print(lemmatization.lemmatize("feet"))       
print(lemmatization.lemmatize("mice"))       
print(lemmatization.lemmatize("cars"))        
print(lemmatization.lemmatize("geese"))       
print(lemmatization.lemmatize("wolves"))      
print(lemmatization.lemmatize("children")) 

#  noun-n
# verb - v
# adjactive - a,
# adverb - r

print(lemmatization.lemmatize("going", "v"))
print(lemmatization.lemmatize("going", "a"))
print(lemmatization.lemmatize("going", "r"))
print(lemmatization.lemmatize("going", "n"))


for word in words:
    print(lemmatization.lemmatize(word, "v"))
    
