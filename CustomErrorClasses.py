# Custom Error Classes

class TooManyPagesRead(ValueError): # essentially a copy of ValueError, this is built in
    pass


class Book:
    def __init__(self,name:str,page_count:int) -> None:
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr__(self) -> str:
        return (
            f"Book {self.name}, read {self.pages_read} pages out of {self.page_count}"
        )
    
    def read(self, pages:int):
        if self.pages_read + pages > self.page_count: 
            #ValueError
            raise TooManyPagesRead(
                f"You tried to read {self.pages_read+pages} pages, but this book only contains {self.page_count} pages."
            )
        self.pages_read+=pages
        print(
            f"You've read {self.pages_read} of a total of {self.page_count} of the {self.name} Book"
        )

py101 = Book("Python 101",50)

try:
    py101.read(30)
    py101.read(1000)
except TooManyPagesRead as e:
    print(e)
