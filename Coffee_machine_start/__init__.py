class User:
    #pass #Służy do zamkończenia klasy nawet jeżeli jest tam błąd to progrma zadziała bez tej classy lub definicji
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 #parametr domyślny
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "Angela")
user_2 = User("002", "Jack")
user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# class Car:
#     def __init__(self,seats):
#         self.seats = seats (jeżeli fnkcja zawiera obiekty to jest metodą)
#
#
#     def enter_race_mode():
#        self.seats = 2
# my_car = Car(5)


# user_1.id = "001" #atrybut
# user_1.username = "angela"

print(user_1.username) #atrybut user name istnieje w obiekcie user_1




#Klasa powinna mieć nazwę z dużj litery na kazdym wyrazie
# to się nazywa PascalCase

# PascalCase - do class
# camelCase - do większości w Pythonie
# snake_case - do innych rzeczy

# #specjalna funkcja
# class Car:
#     def __init__(self):
#         #initialise attributes

