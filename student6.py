class Student:
    def __init__(self, name, house, patronus): # Constructor to initialize name and house
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherine"]:
            raise ValueError("Invalid house")
        self.name = name # Instance variable for name
        self.house = house # Instance variable for house
        self.patronus = patronus

    def __str__(self): # String representation of the object
        return f"{self.name} from {self.house}" # Return formatted string
    
    def charm(self):
        match self.patronus:
            case 'stag':
                return '🐴'
            case 'otter':
                return '🦦'
            case 'Jack Russel terreir':
                return '🐶'
            case _:
                return '🥍'


def main():
    student = get_student() # Get an instance of Student
    print("Expecto patronus")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student = Student(name, house, patronus) # Create an instance of Student
    return student # Return the instance

if __name__ == "__main__":
    main()