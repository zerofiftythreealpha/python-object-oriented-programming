# class Dog:
#     def __init__(self, name, breed, owner):
#         self.name = name
#         self.breed = breed
#         self.owner = owner

#     def bark(self):
#         print("Woof woof")

# class Owner:
#     def __init__(self, name, address, contact_number):
#         self.name = name
#         self.address = address
#         self.phone_number = contact_number
        
# owner1 = Owner("Danny", "122 Springfield Drive", "888-999")
# dog1 = Dog("Bruce", "Terrier", owner1)
# # dog1.bark()
# # print(dog1.name)
# # print(dog1.breed)
# print(dog1.owner.name)


# owner2 = Owner("Sally", "122 Springfield Drive", "888-999")
# dog2 = Dog("Freya", "Greyhound", owner2)
# # dog2.bark()
# # print(dog2.name)
# # print(dog2.breed)
# print(dog2.owner.name)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello my name is {self.name} and I am {self.age} years old")


# person1 = Person("Alice", 30)
# person1.greet()

# person2 = Person("Bob", 42)
# person2.greet()

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # double underscore makes the attribute of a class private
        self.password = password

    # def say_hi_to_user(self, user):
    #     print(f"Sending message to {user.username}: Hi {user.username} its {self.username}")

    # def get_email(self):
    #     return self._email

    # def clean_email(self):
    #     return self.__email.lower().strip()
    # def get_email(self):
    #     return self.__email

    # def set_email(self, new_email):
    #     if "@" in new_email:
    #         self.__email = new_email
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email

    
        

user1 = User("dantheman", "dan@gmail.com", "123")
# user2 = User("batman", "bat@hotmail.com", "abc")
print(user1.get_email())
# user1.say_hi_to_user(user2)