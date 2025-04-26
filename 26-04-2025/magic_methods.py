# Dunder or magic methods in Python
# Python Magic methods are the methods starting and ending with double underscores ‘__’. They are defined by built-in classes in Python and commonly used for operator overloading. 

# They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.

class Book:
    
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return  self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return  self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title 
        if key == "author":
            return self.author
        if key == "num_pages":
            return self.num_pages
        
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K. Rowling", 400)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 410)

print(book1.title)
print(book1.author)
print(book1.num_pages)

print(book2.title)
print(book2.author)
print(book2.num_pages)

print(book3.title)
print(book3.author)
print(book3.num_pages)

print(book1)
print(book2)
print(book3)

print(book1 == book2)
print(book2 == book2)

print(book1 < book2) 
print(book2 + book3)

print("Lion" in book3)
print("Harry" in book1)
print("witch" in book2)
print("Harry" in book2)

print(book1["title"])
print(book2["title"])
print(book3["title"])

print(book1["author"])
print(book2["author"])
print(book3["author"])

print(book1["num_pages"])
print(book2["num_pages"])
print(book3["num_pages"])
