def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def main():
    print("=== Simple Calculator ===")
    operations = {
        "1": ("Addition",       add),
        "2": ("Subtraction",    subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division",       divide),
    }
    while True:
        print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Quit")
        choice = input("Choose: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in operations:
            try:
                a = float(input("First number: "))
                b = float(input("Second number: "))
                name, func = operations[choice]
                print(f"Result: {func(a, b)}")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
