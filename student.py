# class Student:
#     name:"Agnes"
#     age:20
#     code:79
#     school:"Akirachix"

class Student:
    school="Akirachix"
    def __init__(self,first_name,last_name,age,country,code):
        self.first_name= first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.code=code

    def greeting_student(self):
        greeting = f" Hello{ self.first_name} welcome to {self.school}.Your code is{self.code }"

    def year_of_birth(self):
        return f" Hello {self.first_name} you were born in {self.age}"
    
    #Method to show full name

    def full_names(self):
        return f" Hello my name is {self.first_name}+ {self.last_name}"
    
     #Method to show the initials 
    def show_initials(self):
        return self.first_name[0] + self.last_name[0]
    
     #Method to enrol student to a class
    def enrol(self, class_name):
        print(f"{self.first_name} {self.last_name} has been enrolled in {class_name}.")

    #Method to check if student is a minor
        def is_minor(self):
            return self.age < 18
