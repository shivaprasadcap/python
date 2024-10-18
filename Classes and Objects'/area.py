class Area:

    def __init__(self):
        print("Shapes: ")
        print("1. Triangle.")
        print("2. Circle.")
        print("3. Rectangle.")
        
        option = input("Enter shape to find area (1/2/3): ")

        if option == '1':
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            areat = 0.5 * base * height
            print(f"Area of triangle: {areat}")

        if option == '2':
            rad = float(input("Enter radius: "))
            areac = 3.14 * rad * rad
            print(f"Area of circle: {areac}")

        if option == '3':
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))
            arear = 0.5 * length * breadth
            print(f"Area of rectangle: {arear}")

ob1 = Area()
    