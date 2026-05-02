from rectangle import Rectangle

def main():
    print("Land Measurement Calculator")
    print("Note: Enter values in meters \n")

    length = float(input("Enter length : "))
    width = float(input("Enter width : "))

    if length <= 0 or width <= 0:
        print("Length and width cannot be negative.")
        return

    rect = Rectangle(length, width)

    area = rect.cal_area()
    perimeter = rect.cal_perimeter()

    print(f"Area: {area} square meters (m²)")
    print(f"Perimeter: {perimeter} meters (m)")


if __name__ == "__main__":
    main()