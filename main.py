from pydantic import BaseModel, Field, EmailStr, field_validator
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


#2. Automatic conversion (Avtomatik konvertatsiya)

class User(BaseModel):
    age: int
    
user=User(age="25")
print(user)

class Product(BaseModel):
    price: float

product=Product(price="19.99")
print(product)


#3. Giving list, dict, set (Ro‘yxat, lug‘at va to‘plam)

class ShoppingCart(BaseModel):
        items: list[str]
s=ShoppingCart(items=["olma", "behi", "anor"])
print(s)

class Invertory(BaseModel):
    stock: dict[str, int]
    
i=Invertory(stock={
    "olma": 10,
    "behi": 5,
    "anor": 7
})
print(i)
    
class UniqueTags(BaseModel):
    tags: set[str]
u=UniqueTags(tags=["a", "a", "b", "c", "b"])
print(u)

#4. Required, optional fields (Majburiy va ixtiyoriy maydonlar)
class Person(BaseModel):
    name: str
    nickname: str | None = None
p=Person(name="Ali")
print(p)

class Car(BaseModel):
    make: str
    model: str
    color: str = "black"
c=Car(make="Chevrolet", model="Spark")
print(c)    
    
#5. Email validation (Email tekshiruvi)
class Customer(BaseModel):
    email: EmailStr
custom=Customer(email="adb@org.uz")
print(custom)
 
class Employee(BaseModel):
    email: EmailStr
    work_email: EmailStr
emp=Employee(email="employ@gmail.com", work_email="work@gmail.com")
print(emp)
    

#6. Field constraints (cheklovlar: ge, le, gt, min_length, max_length, pattern)

class Product(BaseModel):
    price: float =Field(gt=0)
prod=Product(price=12.3)
print(prod)
class User(BaseModel):
    username: str =Field(
        ...,
        pattern=r"^[a-zA-Z0-9_]+$"
    )
user=User(username="Ali123_")
print(user)
class Review(BaseModel):
    rating: int=Field(ge=1, le=5)
reviv=Review(rating=5)
print(reviv)

#7. Field va required combination

class Profile(BaseModel):
    name: str             
    bio: str | None = None
    age: int = Field(gt=18) 

prof = Profile(
    name="Ali",
    age=25
)
print(prof)

class Order(BaseModel):
    id: int
    status: str = Field(default="pending")
    total: float = Field(gt=0) 
    
order = Order(
    id=101,
    total=250.75
)
print(order)

#ustoz Kompyuterim ustada edi dushanbagacha yakunlab qo'yaman
          
