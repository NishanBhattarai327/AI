# Write a Python program to create a person class. Include attributes like name, country and date of
# birth. Implement a method to determine the person's age.
from datetime import date
from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        
        try:
            date_format = "%m-%d-%Y"
            self.dob = datetime.strptime(dob, date_format).date()  # Date of birth
        except Exception as e:
            print(f"An error occurred: {e}")
            raise Exception('Invalid DOB')

    def age(self):
        days = (date.today() - self.dob).days
        yrs_old = int(days/365.25)
        return f'{self.name.split(' ')[0]}\'s age is {yrs_old} year.'

def main():
    try:
        name = input("Enter your name: ")
        country = input("Enter your country name: ")
        dob = input("Enter your date of birth (mm-dd-yyyy): ")
        person = Person(name, country=country, dob=dob)
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    print(person.age())

if __name__ == '__main__':
    main()