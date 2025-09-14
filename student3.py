def main():
    student = get_student()
    if student[0] == 'Padma':
        # This will drop an error if get_student returns a tuple
        # Because tuples are immutable
        student[1] = 'Ravenclaw'
    print(f"{student[0]} from {student[1]}")

def get_student():
    return input("Name: "), input("House: ")

if __name__ == "__main__":
    main()