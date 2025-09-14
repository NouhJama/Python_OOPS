class Student:
    def __init__(self, name, house): # Constructor to initialize name and house
        self.name = name # Instance variable for name
        self.house = house # Instance variable for house


def main():
    student = get_student() # Get an instance of Student
    if student.name == "Padma": # Access name using dot notation
        student.house = "Ravenclaw" # Modify house using dot notation   
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # Create an instance of Student
    return student # Return the instance

if __name__ == "__main__":
    main()