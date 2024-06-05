from datetime import date

#Difine a class person
class Person:
    def __init__(self,name,country,date_of_birth):
        #private variables
        self.__name = name
        self.__country = country
        self.__date_of_birth = date_of_birth

    def set_name(self,name):
        self.__name = name

    def set_country(self,country):
        self.__country = country

    def set_date_of_birth(self,birthday):
        self.__date_of_birth = birthday

    def get_name(self):
        return self.__name
    
    def get_country(self):
        return self.__country
    
    def get_date_of_birth(self):
        return self.__date_of_birth
    
    def display_details(self):
        print(f"Name: {self.__name}\nCountry: {self.__country}\nDate of Birth: {self.__date_of_birth}")

    def calculate_person_age(self):
        today = date.today()
        age = today.year - self.__date_of_birth.year
        if today < date(today.year,self.__date_of_birth.month,self.__date_of_birth.day):
            age -= 1

        return age

#define objects
person_1 = Person("John","America", date(1988,2,24))
danushka = Person("Dhanushka Lakruwan","Sri Lanka", date(2000,8,17))


danushka.display_details()
print(f"Age is {danushka.calculate_person_age()}")




                 