def main():
    student = get_student()
    if student['name'] == "Padma":
        student['house'] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    # Create an empty dictionary
    student = {}
    student["name"] = input("Name: ") # Get the name from user
    student["house"] = input("House: ") # Get the house from user
    return student # Return the dictionary

if __name__ == "__main__":
    main()