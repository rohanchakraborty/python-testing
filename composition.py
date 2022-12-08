class BookShelf:
  def __init__(self,*books):
    self.books = books

  def __str__(self):
    return f"Book shelf with {self.quantity} books"

shelf = BookShelf(11)

# When inheritance, A book is a book shelf is a book but something more or less
#No use to inherit if we're not gonna use it, I mean a child and parent have a inheritance relationship but a bookshelf and book are just two different things
#We can say that a bookshelf is composed out of a lot of books
#Voila! Composition!

class Book:
  def __init__(self,name):
    self.name = name
    #self.quantity = quantity 
    #super().__init__(quantity)#inherit from super
  
  def __str__(self):
    return f "Book {self.name}"
  

book = Book("book1")
book2 = Book("book2)
shelf = BookShelf(book,book2) # composition  
    
