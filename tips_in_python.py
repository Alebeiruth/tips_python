# 00 Tips
if 176 <= boxeador_peso <= 200:

#Primeira parte: 176 <= boxeador_peso: Verifica se o valor de boxeador_peso é maior ou igual a 176.

#Segunda parte: boxeador_peso <= 200: Verifica se o valor de boxeador_peso é menor ou igual a 200.

# 01 Tips

class Dog:
  pass

dog = Dog()

# the better way

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

my_dog = Dog("Joe", 5)

# 02 Tip

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

my_dog = Dog("Joe", 5)
print(dog)

# the beeter way

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
   def __str__(self):
     return f"Dog(name={self.name} ge={self.age})"

my_dog = Dog("Joe", 5)
print(dog)

# 03 Tip

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

dog = Dog("rocky", 5)

# the better way
print(dog.__dict__) 
# ouypu {"name": "rocky", "age":5}

# 04 Tip
class Rectangle:
  def __initi__(self, altura, largura):
    self.altura = altura
    self.largura = largura
    
  def area(self):
    return self.altura * self.largura

class Square(Rectangle):
  def __init(self, altura):
    super().__init__(altura, altura)

s = Square(5)
print(s.altura, s.largura)
print(s.area())

# 05 Tip

lass Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduce(self):
    print(f'my name is {self.name} and my age is {self.age}')

dog = Dog('rocky', 5)
dog.introduce()

# the beeter way

class Dog:
  
  all_dog_names = []    # this is a class attribute

  def __init__(self, name, age):
    self.name = name
    self.age = age
    Dog.all_dog_names.append(name)

  @classmethod
  def get_all_dog_names(cls):
    return cls.all_dog_names

dog = Dog('rocky', 5)
dog = Dog('remy', 5)
dog = Dog('fifi', 5)

print(Dog.get_all_dog_names())

class Dog:
  @staticmethod
  def get_equivalent_age(dog_age):
    human_age = dog_age * 7
    return human_age

print(Dog.get_equivalent_age(5))

# 06 tips

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Dog:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age

  @property
  def name(self):
    return self.__name

  @property
  def age(self):
    return self.__age


class Dog:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, new_name):
    self.__name = new_name

  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, new_age):
    self.__age = new_age
