from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator, computed_field
from typing_extensions import Annotated
from datetime import date
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
    
movie = Movie(name="Olamlarga nur sochgan oy", director="Moustapha Akkad", duration_minutes="178")
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

class Inventory(BaseModel):
    stock: dict[str, int]
    
i=Inventory(stock={
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

          
#8. @field_validator

class Person(BaseModel):
    birth_year: int
    
    @field_validator("birth_year")
    @classmethod
    
    def filt_birth(cls, v):
        if v < 1900:
            raise ValueError("Tug'ilgan ku 1900 dan keyingi bolishi kerak!")
        else:
            return v
        
    
class Product(BaseModel):
    price: int
    
    @field_validator("price")
    @classmethod
    
    def filt_price(clas, v):
        if v > 1000:
            print("Price 1000 dan katta!")
        else:
            return v


#9. @model_validator, modes after, before    
 
class Event(BaseModel):
    start_date: date
    end_date: date
    
    @model_validator(mode="before")
    @classmethod
    def filt_data(cls, data):
        start = data.get("start_date")
        end = data.get("end_date")
        
        if start > end:
            raise ValueError("error")
        else:
            return data
    

class Transaction(BaseModel):
    amount: int
    currency: str
    
    @model_validator(mode="after")
    
    def filt_abs(self):
        if self.amount < 0:
            raise ValueError("error")
        else:
            return self
        


#10. Nested models (Ichma-ich modellar)

class Address(BaseModel):
    street: str
    city: str
    zipcode: int
    
class User(BaseModel):
    name: str
    email: EmailStr
    address: Address

class Item(BaseModel):
    name: str
    price: int
    
class Order(BaseModel):
    user: User
    items: list[Item]


#11. model_dump, model_dump_json, exclude, include, exclude_none
    
class User(BaseModel):
    name: str
    email: EmailStr
    password: str   
       
u = User(name="Ali", email="ali@gmail.com", password="12345a")
print(u.model_dump(include={"name", "email"}))

class Item(BaseModel):
    name: str
    price: int

class Order(BaseModel):
    id: int
    user: User
    items: list[Item]
    discount: int | None=None
    
o=Order(id=1, user=User(name="Ali", email="ali@gmail.com", password="12345a"), items=[Item(name="Book", price=100), Item(name="Pen", price=20)])
print(o.model_dump_json(exclude_none=True))


#12. Field alias, model_dump(by_alias=True), "populate_by_name": True

class User(BaseModel):
    first_name: str =Field(alias="fName")
    
u = User(first_name="Ali")
print(u.model_dump(by_alias=True))

class Product(BaseModel):
    product_id: int =Field(alias="pid")
    
    model_config = {"populated_by_name": True}
p = Product(product_id=2)
print(p.product_id)
  
  
    
#13. @computed_field bilan @property

class Rectangle(BaseModel):
    width: float
    height: float
    
    @computed_field
    @property
    def area(self) -> float:
        return self.width * self.height
    
class Invoice(BaseModel):
    unit_price: float
    quantitiy : int
    
    @computed_field
    @property
    def total_price(self) -> float:
        return self.unit_price * self.quantitiy
    


#14. Model_config: "extra": "forbid", "strict": True, "frozen": True   
    
class User(BaseModel):
    first_name: str
    
    model_config = {
        "extra": "forbid"
    }
    
class Product(BaseModel):
    name : str
    
    model_config = {
        "strict":True
    }    
    
class ConfigTest(BaseModel):
    title : str
    
    model_config = {
        "frozen": True }
    


#15. model_validate(), model_validate_json(), "from_attributes": True

class Person(BaseModel):
    name : str
    
json_data = '{"name": "Ali"}'
    
p = Person.model_validate_json(json_data)
print(p)

class User(BaseModel):
    id: int
    name: str
    age: int

    model_config = {
        "from_attributes": True
    }


#16. Custom types

def Color(v: str) -> str:     # Color tipini yaratib, faqat "red", "green", "blue" qabul qiladigan qilib yozing.
    allowed = {"red", "green", "blue"}
    if v not in allowed:
        raise ValueError("""Color tipi faqat: "red", "green", "blue" bo'lishi kerak""")
    return v

def phone(v: str) -> str:  #PhoneNumber tipini yaratib, faqat raqam va + bilan boshlangan telefon raqamini qabul qiling.
    if not v.startswith("+"):
        raise ValueError("faqat + bilan boshlangan bo'lishi kerak!")
    return v

#17. Custom error messages

class User(BaseModel):    #Age maydoni uchun maxsus xato yozing: agar 18 dan kichik bo‘lsa "Foydalanuvchi 18 yoshdan kichik bo‘la olmaydi".
    age: int

    @field_validator("age")
    @classmethod
    def check_age(cls, v):
        if v < 18:
            raise ValueError("Yosh 18 dan katta bolishi kerak")
        return v

class Username(BaseModel):  #Username maydoni uchun pattern xatosi yuzaga kelganda "Foydalanuvchi nomi faqat harflar va raqamlardan iborat bo‘lishi kerak" xabarini chiqarish.
    name: str
    
    @field_validator("name")
    @classmethod
    def check_name(cls, v: str):
        if not v.isalnum():
            raise ValueError("faqat harflar yoki raqamlardan iborat bo'lishi kerak!")
        return v
            