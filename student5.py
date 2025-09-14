class Student:
    ... # IGNORE


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student()
    student.name = name
    student.house = house   
    return student

if __name__ == "__main__":
    main()