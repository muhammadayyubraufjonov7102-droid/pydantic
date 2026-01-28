from pydantic import BaseModel
#1. Basic model (Asosiy model)

class Book(BaseModel):
    title: str
    author: str
    year: int
    
book = Book(title="Ikki eshik orasi", author="O'.Xoshimov", year="2003")
print(book)

class Movie(BaseModel):
    name: str
    director: str
    duration_minutes: int
    
movie = Movie(name="Olamlarga nur sochgan oy", director="Moustapha Akkad", duration_minutesr="178")
print(movie)

        