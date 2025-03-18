class Person:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def get_age(self):
        return self.__age

    @property # Getter for computed attribute
    def is_adult(self):
        return self.__age >= 40

# Usage
person = Person("balmond", "Smith", 50)
print(f"Full Name: {person.get_full_name()}")
print(f"Age: {person.get_age()}")
print(f"Is Adult: {person.is_adult}")