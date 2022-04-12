class Person:

    def __init__(self,name,surname,age,id_number):
        self.name = name
        self.surname = surname
        self.id_number = id_number
        self.age = age

    def information(self):
        return f'{self.name}, {self.surname}, {self.age}, {self.id_number}'
 
class Patient(Person):

    def __init__(self,coming_dates,appointment_history,total_debt):
        self.coming_dates = coming_dates
        self.appointment_history = appointment_history
        self.total_debt = total_debt

class Arzt(Person):

    def __init__(self,diary,area_of_expertise):
        self.diary = diary
        self.area_of_expertise = area_of_expertise

class Termin(Patient,Arzt):

    def __init__(self,date,time,doctor,party,cost,description):
        self.date = date
        self.time = time
        self.doctor = doctor
        self.party = party
        self.cost = cost
        self.description = description 

# person1 = Person("Kerem","Ekenci","10000000",23)
person1 = Person(input("Vorname: "),input("Nachname: "),input("Alter: "),input("ID-Nummer: "))
print(person1.information())



