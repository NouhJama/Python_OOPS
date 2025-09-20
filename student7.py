class Student:
    def __init__(self, name, house): # Constructor to initialize name and house
        self.name = name # Instance variable for name
        self.house = house # Instance variable for house

    def __str__(self): # String representation of the object
        return f"{self.name} from {self.house}" # Return formatted string
    
    #Getter methods
    @property
    def house(self):
        return self._house # Return the house
    
    #Setter methods
    @house.setter
    def house(self, house): # Setter for house
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house # Set the house


def main():
    student = get_student() # Get an instance of Student
    student.house = "Number Four, Privet Drive" # Update the house using the setter
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # Create an instance of Student
    return student # Return the instance

if __name__ == "__main__":
    main()