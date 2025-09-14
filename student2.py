def main():
    name, house = get_student()
    print(f"{name} from {house}")

def get_student():
    return [input("Name: "), input("House: ")]

if __name__ == "__main__":
    main()