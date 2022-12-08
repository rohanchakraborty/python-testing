def list_avg(sequence:list) -> float: # sequence has to be a list and the output of the function is a float
  return sum(sequence)/len(sequence)


# this can also be implemented using importing from typing

from typing import List

# implement is class

class Book:
  pass

class BookShelf:
  def __init__(self,books:List[Book]):  # type hinting :: books are a List of book class's objectes
    self.books = books
  
  def __str__(self) -> str: # expected output is str
    return f"Bookshelf with {len(self.books)} books."
  
  
